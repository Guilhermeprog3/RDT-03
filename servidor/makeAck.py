from calculate_sum import calculate_checksum
def make_ack(seqnum):
    ack_data = f"ACK{seqnum}".encode('utf-8')
    checksum = calculate_checksum(ack_data)
    return bytes([checksum]) + ack_data