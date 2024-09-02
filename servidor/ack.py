def is_ack(packet, expected_acknum):
    ack_data = packet[1:].decode('utf-8')
    return ack_data == f'ACK{expected_acknum}'