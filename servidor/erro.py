import socket
from pkt import make_pkt
from corrupt import is_corrupt
from ack import is_ack
import tkinter as tk
from client import start_client

def simulate_error(error_type, ip_entry, port_entry, expression_entry, text_widget):
    server_ip = ip_entry.get()
    server_port = int(port_entry.get())
    server_address = (server_ip, server_port)
    expression = expression_entry.get()

    if error_type == 'corrupt':
        # Simula a corrupção do pacote
        start_client(ip_entry, port_entry, expression_entry, text_widget, simulate_error=error_type)
    elif error_type == 'loss':
        # Simula a perda do pacote
        simulate_loss_error(server_ip, server_port, expression, text_widget)
    elif error_type == 'checksum_loss':
        start_client(ip_entry, port_entry, expression_entry, text_widget, simulate_error=error_type)
    elif error_type == 'packet_corruption':
        start_client(ip_entry, port_entry, expression_entry, text_widget, simulate_error=error_type)
    elif error_type == 'checksum_corruption':
        start_client(ip_entry, port_entry, expression_entry, text_widget, simulate_error=error_type)

def simulate_loss_error(server_ip, server_port, expression, text_widget):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Inicia o cliente para simular o timeout e retransmissão
        text_widget.insert(tk.END, "Simulando perda de pacote...\n", "error_info")
        
        # Simula o timeout aguardando sem enviar o pacote
        timeout_interval = 2
        sock.settimeout(timeout_interval)
        
        try:
            # Isso não envia o pacote, apenas faz o cliente aguardar um timeout
            text_widget.insert(tk.END, "Pacote não enviado. Aguardando timeout no cliente...\n", "error_info")
        except socket.timeout:
            text_widget.insert(tk.END, "Timeout simulado no servidor. O cliente deve retransmitir o pacote.\n", "error_info")
