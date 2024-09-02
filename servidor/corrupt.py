from calculate_sum import calculate_checksum
def is_corrupt(packet):
    received_checksum = packet[0]
    data = packet[1:]
    calculated_checksum = calculate_checksum(data)
    return received_checksum != calculated_checksum