import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

newfile = sys.argv[1]
os.system("rm -r summary_"+newfile[:-4])
os.system("mkdir summary_"+newfile[:-4])
filename = "../csv_files/"+newfile
data = pd.read_csv(newfile, encoding = 'latin-1')
os.chdir("summary_"+newfile[:-4])
source = data["ip.src_host"].value_counts().idxmax()
print(source)
print(data.iloc[0])

#GRAPH 1 below ------------------------------------------------

plt.title("Number of outgoing packets")
data["ip.src_host"].value_counts().drop(source)[:20].plot.bar()
plt.xticks(rotation=40, ha='right')
plt.tight_layout()
plt.savefig("barchart_outgoing_num.png") 

#GRAPH 2 below ------------------------------------------------

plt.title("Outgoing packet addresses, packet size")
data["_ws.col.Length"].groupby(data["ip.src_host"]).sum().sort_values(0)[:20].plot.bar()
plt.xticks(rotation=40, ha='right')
plt.tight_layout()
plt.savefig("bar_outgoing_packet_size.png")

#GRAPH 3 below ------------------------------------------------

plt.title("Number of incoming packets")
data["ip.dst_host"].value_counts().drop(source)[:20].plot.bar()
plt.xticks(rotation=40, ha='right')
plt.tight_layout()
plt.savefig("barchart_incoming_num.png") 

#GRAPH 4 below ------------------------------------------------

plt.title("Incoming packet addresses, packet size")
data["_ws.col.Length"].groupby(data["ip.dst_host"]).sum().sort_values(0)[:20].plot.bar()
plt.xticks(rotation=40, ha='right')
plt.tight_layout()
plt.savefig("bar_incoming_packet_size.png")

#GRAPH 5 below ------------------------------------------------
plt.title("Ratio of outgoing packets/incoming packets with packet size")



