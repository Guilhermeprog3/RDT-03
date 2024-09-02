from calculate_sum import calculate_checksum
import tkinter as tk

def make_pkt(seqnum, data):
    seqnum_str = str(seqnum)
    data_bytes = f'{seqnum_str}{data}'.encode('utf-8')
    checksum = calculate_checksum(data_bytes)
    return bytes([checksum]) + data_bytes