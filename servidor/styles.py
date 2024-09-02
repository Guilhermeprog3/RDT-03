import tkinter as tk
from tkinter import scrolledtext, Frame, font
from start import start_server
from client import start_client
from erro import simulate_error
from server import simulate_packet_loss
# Função para mostrar o frame do servidor
def show_server_frame():
    client_frame.pack_forget()
    server_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Função para mostrar o frame do cliente
def show_client_frame():
    server_frame.pack_forget()
    client_frame.pack(fill="both", expand=True, padx=10, pady=10)

root = tk.Tk()
root.title("Calculadora Remota - Cliente e Servidor")

# Estilos e Configurações Visuais
bg_color = "#34495e"
fg_color = "#ecf0f1"
btn_color = "#3498db"
font_style = font.Font(family="Arial", size=12, weight="bold")

root.configure(bg=bg_color)

# Frame principal para alternar entre servidor e cliente
main_frame = Frame(root, bg=bg_color)
main_frame.pack(fill="both", expand=True, pady=10)

# Botões para alternar entre cliente e servidor
btn_server = tk.Button(main_frame, text="Servidor", command=show_server_frame, font=font_style, bg=btn_color, fg=fg_color)
btn_server.pack(side="left", padx=20)

btn_client = tk.Button(main_frame, text="Cliente", command=show_client_frame, font=font_style, bg=btn_color, fg=fg_color)
btn_client.pack(side="right", padx=20)

# Frame do Servidor
server_frame = Frame(root, bg=bg_color)

server_ip_label = tk.Label(server_frame, text="IP do Servidor:", bg=bg_color, fg=fg_color, font=font_style)
server_ip_label.pack(pady=5)

server_ip_entry = tk.Entry(server_frame, font=font_style, bg=fg_color, fg=bg_color)
server_ip_entry.pack(pady=5, fill='x')

server_port_label = tk.Label(server_frame, text="Porta do Servidor:", bg=bg_color, fg=fg_color, font=font_style)
server_port_label.pack(pady=5)

server_port_entry = tk.Entry(server_frame, font=font_style, bg=fg_color, fg=bg_color)
server_port_entry.pack(pady=5, fill='x')

server_button = tk.Button(server_frame, text="Iniciar Servidor", command=lambda: start_server(server_ip_entry, server_port_entry, server_text_area), font=font_style, bg=btn_color, fg=fg_color)
server_button.pack(pady=10)

server_text_area = scrolledtext.ScrolledText(server_frame, wrap=tk.WORD, width=50, height=10, bg=fg_color, fg=bg_color, font=font_style)
server_text_area.pack(pady=10)

# Botões de Simulação de Erros no Servidor
error_frame_server = Frame(server_frame, bg=bg_color)
error_frame_server.pack(pady=10)

# Botão para simular perda de pacote
loss_button = tk.Button(error_frame_server, text="Simular Perda de Pacote", command=lambda: simulate_packet_loss(server_text_area), font=font_style, bg=btn_color, fg=fg_color)
loss_button.grid(row=0, column=0, padx=5, pady=5)

# Frame do Cliente
client_frame = Frame(root, bg=bg_color)

client_ip_label = tk.Label(client_frame, text="IP do Servidor:", bg=bg_color, fg=fg_color, font=font_style)
client_ip_label.pack(pady=5)

client_ip_entry = tk.Entry(client_frame, font=font_style, bg=fg_color, fg=bg_color)
client_ip_entry.pack(pady=5, fill='x')

client_port_label = tk.Label(client_frame, text="Porta do Servidor:", bg=bg_color, fg=fg_color, font=font_style)
client_port_label.pack(pady=5)

client_port_entry = tk.Entry(client_frame, font=font_style, bg=fg_color, fg=bg_color)
client_port_entry.pack(pady=5, fill='x')

expression_label = tk.Label(client_frame, text="Expressão:", bg=bg_color, fg=fg_color, font=font_style)
expression_label.pack(pady=5)

expression_entry = tk.Entry(client_frame, font=font_style, bg=fg_color, fg=bg_color)
expression_entry.pack(pady=5, fill='x')

send_button = tk.Button(client_frame, text="Enviar Expressão", command=lambda: start_client(client_ip_entry, client_port_entry, expression_entry, client_text_area), font=font_style, bg=btn_color, fg=fg_color)
send_button.pack(pady=10)

client_text_area = scrolledtext.ScrolledText(client_frame, wrap=tk.WORD, width=50, height=10, bg=fg_color, fg=bg_color, font=font_style)
client_text_area.pack(pady=10)

# Botões de Simulação de Erros no Cliente
error_frame_client = Frame(client_frame, bg=bg_color)
error_frame_client.pack(pady=10)

# Botão para simular pacote corrompido
corrupt_button = tk.Button(error_frame_client, text="Simular Pacote Corrompido", command=lambda: simulate_error('corrupt', client_ip_entry, client_port_entry, expression_entry, client_text_area), font=font_style, bg=btn_color, fg=fg_color)
corrupt_button.grid(row=0, column=0, padx=5, pady=5)

root.mainloop()
