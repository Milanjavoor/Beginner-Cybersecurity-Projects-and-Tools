from collections import  defaultdict
import csv 
from datetime import timedelta,datetime

logfile=r"C:\Users\ADMIN\Documents\suspiciousip.txt"

failedlogin_threshold=5
time_threshold=5

failed_logis=defaultdict(list)

with open (logfile,"r") as file:
    for line in file :
        line=line.strip()
        if not line:
            continue

        parts=line.split()

        if len(parts)<4:
            continue

        event=parts[2]

        timestamp_data=parts[0]+" "+parts[1]

        ipaddress=parts[3]

        if event!="FAILED_LOGIN":
            continue

        time=datetime(timestamp_data,"Y-m-d H:M:S")


alerts=[]
