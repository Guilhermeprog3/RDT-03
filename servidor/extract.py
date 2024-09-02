def extract_data(packet):
    return packet[2:].decode('utf-8')