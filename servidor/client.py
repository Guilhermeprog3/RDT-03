import socket
from pkt import make_pkt
from corrupt import is_corrupt
from ack import is_ack
import tkinter as tk
import random

seqnum = 0

def corrupt_checksum(packet):
    corrupted_packet = bytearray(packet)
    corrupted_packet[0] = (corrupted_packet[0] + random.randint(1, 255)) % 256
    return bytes(corrupted_packet)

def start_client(ip_entry, port_entry, expression_entry, text_widget, simulate_error=None):
    global seqnum  
    server_ip = ip_entry.get()
    server_port = int(port_entry.get())
    expression = expression_entry.get()
    server_address = (server_ip, server_port)
    timeout_interval = 2
    error_simulated = False  

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        packet = make_pkt(seqnum, expression) 
        ack_received = False

        while not ack_received:

            if simulate_error == 'corrupt' and not error_simulated:
                corrupted_packet = corrupt_checksum(packet)
                sock.sendto(corrupted_packet, server_address)
                text_widget.insert(tk.END, "Simulação de erro: pacote corrompido enviado.\n", "error_info")
                error_simulated = True
            else:
                sock.sendto(packet, server_address)
                text_widget.insert(tk.END, f"Expressão enviada: {expression}\n", "client_info")

            sock.settimeout(timeout_interval)

            try:
                ack_packet, _ = sock.recvfrom(1024)
                if not is_corrupt(ack_packet) and is_ack(ack_packet, seqnum):
                    text_widget.insert(tk.END, f"ACK {seqnum} recebido\n", "client_info")

                    result_packet, _ = sock.recvfrom(1024)
                    text_widget.insert(tk.END, f"Resultado: {result_packet.decode('utf-8')}\n ----------------------------------------------------------------------------------------\n", "result_info")

                    seqnum = 1 - seqnum
                    ack_received = True
                else:
                    text_widget.insert(tk.END, "ACK incorreto ou pacote corrompido. Retrasmitindo.\n", "error_info")
            except socket.timeout:
                text_widget.insert(tk.END, f"Timeout! Retransmitindo a expressão.\n", "error_info")

