import os
import sys
import csv
from operator import itemgetter
import numpy
import matplotlib.pyplot as plt



#csv file you enter in command line
file = sys.argv[1]
name = file[:-4] + "_new"+".csv"
os.system("rm -r "+name)
with open(file, 'r') as csvfile:
	reader = csv.reader(csvfile)
	next(reader) #removing header 
	newlist = [] #making the list we will append to
	firstline = next(reader)#to get phone ip 
	my_ip = firstline[1]
	start_time = firstline[0]
	csvfile.seek(0)#going back to header
	next(reader)#removing header
	prev_value = ''#initialsing stuff
	size = 0
	length = 0
	for line in reader:
		#setting curr value to the other ip (either dest or src)
		if line[1] != my_ip:
			curr_value = line[1]
		else:
			curr_value = line[2]
		if prev_value == curr_value:
			size = size + int(line[3])
			length = length + 1
		else:
			adding = [str(prev_value) +  " at " +str(start_time[12:-4]) , size, length]
			start_time = line[0]
			prev_value = curr_value
			length = 0
			size = 0
			newlist.append(adding)
sorted_by_size = sorted(newlist, key = itemgetter(1))
sorted_by_length = sorted(newlist, key = itemgetter(2))
#print("sorted by length top 10 ", sorted_by_length[-10:], "\n")
#print("sorted by packet size top 10 ", sorted_by_size[-10:], "\n")
max_length = int(sys.argv[2])

with open(name, 'a') as the_file:
	the_file.write("ips,size,length\n")
	for lists in sorted_by_size[-max_length:]:
		the_file.write(str(lists[0])+ "," +str(lists[1]) + "," + str(lists[2])+ "\n")