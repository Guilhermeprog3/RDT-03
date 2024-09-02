from server import rdt_receiver
import threading
def start_server(ip_entry, port_entry, text_widget):
    server_ip = ip_entry.get()
    server_port = int(port_entry.get())
    server_address = (server_ip, server_port)
    threading.Thread(target=rdt_receiver, args=(server_address, text_widget)).start()