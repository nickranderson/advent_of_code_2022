# -*- coding: utf-8 -*-
input_file = open("C:/Users/Nick Anderson/Desktop/input.txt")
signal = input_file.read()
input_file.close()

#Start of signal
for start_char in range(0,len(signal)-4):
    packet_signal = signal[start_char:start_char+4]
    if len(set(packet_signal)) == 4:
        print(start_char+4)
        break

#Start of message
for start_char in range(0,len(signal)-14):
    packet_signal = signal[start_char:start_char+14]
    if len(set(packet_signal)) == 14:
        print(start_char+14)
        break