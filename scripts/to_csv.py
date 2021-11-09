import pyshark
import os
import sys
import csv


#takes input for file name
pcap = pyshark.FileCapture(sys.argv[1])
filename = sys.argv[1][:-4] + "csv"
#removes csv file if already exists
os.system("rm -r "+filename)
#opening csv file
csvF = open(filename, 'w')
writer = csv.writer(csvF)
writer.writerow(["source IP", "Destination IP", "File size", "Time"])
#iterates through packets
for packet in pcap:
    try: #some packets dont have destination or source ip not sure why. 
        #All packets that dont have source also dont have destination
        dest = packet.ip.dst
        src = packet.ip.src
    except AttributeError:
        dest = "-"
        src = "-"
    size = len(packet)
    time = str(packet.sniff_time)
    #making row and writing to csv
    row = [src, dest, size, time]
    writer.writerow(row)
csvF.close()


