import socket
import tkinter as tk
from corrupt import is_corrupt
from extract import extract_data
from calculate import calculate_expression
from has0 import has_seq0
from has1 import has_seq1
from deliverD import deliver_data
from makeAck import make_ack

simulate_loss = False
loss_simulated = False

def simulate_packet_loss(text_widget):
    global simulate_loss, loss_simulated
    simulate_loss = True
    loss_simulated = False
    text_widget.insert(tk.END, "Simulação de perda de pacote iniciada.\n", "info")

def rdt_receiver(server_address, text_widget):
    global simulate_loss, loss_simulated
    expected_seqnum = 0
    last_ack_pkt = None

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(server_address)
        text_widget.insert(tk.END, f"Servidor iniciado no endereço {server_address}\n----------------------------------------------------------------------------------------\n", "server_info")

        while True:
            try:
                packet, addr = sock.recvfrom(1024)
                text_widget.insert(tk.END, f"Pacote recebido\n", "server_info")

                if simulate_loss and not loss_simulated:

                    loss_simulated = True
                    text_widget.insert(tk.END, "Simulação de perda: ACK não enviado.\n", "error_info")
                    continue 

                if not is_corrupt(packet):
                    if (expected_seqnum == 0 and has_seq0(packet)) or (expected_seqnum == 1 and has_seq1(packet)):
                        expression = extract_data(packet)
                        result = calculate_expression(expression)
                        deliver_data(f"Resultado: {result}", text_widget)

                        last_ack_pkt = make_ack(expected_seqnum)
                        sock.sendto(last_ack_pkt, addr)
                        sock.sendto(str(result).encode('utf-8'), addr)
                        text_widget.insert(tk.END, f"ACK {expected_seqnum} enviado\n", "server_info")

                        expected_seqnum = 1 - expected_seqnum 
                        text_widget.insert(tk.END, f"Esperando seqnum {expected_seqnum} agora\n ----------------------------------------------------------------------------------------\n", "server_info")

                        if loss_simulated:
                            simulate_loss = False
                            loss_simulated = False
                    else:
                        text_widget.insert(tk.END, f"Seqnum incorreto: esperado {expected_seqnum}, recebido {packet[1] - ord('0')}\n", "error_info")
                        text_widget.insert(tk.END, "Enviando ultimo ack da memoria\n", "error_info")
                        if last_ack_pkt:
                            sock.sendto(last_ack_pkt, addr)
                else:
                    text_widget.insert(tk.END, "Pacote corrompido detectado\n", "error_info")

                    text_widget.insert(tk.END, "Enviando ultimo ack da memoria\n", "error_info")
                    if last_ack_pkt:
                        sock.sendto(last_ack_pkt, addr)
            except Exception as e:
                text_widget.insert(tk.END, f"Erro no servidor: {str(e)}\n", "error_info")
