import sys
import os


file = sys.argv[1]
name = file[:-4] + "_new"+".csv"
os.system("python3 grouping.py "+ file + " " + sys.argv[2])
#"do what rudra needs for comps" - David Anderson, Women and Gender Studies major
os.system("Rscript --vanilla make_graphs.r " + name + " " + sys.argv[3])