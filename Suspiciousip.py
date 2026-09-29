from collections import  defaultdict

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

# ----------------------------------------- Find the suspicious ips --------------------------------------------------------------------------------------------
alerts=[]


for ip_addresses,timestamps in failed_logis.items():

    timestamps.sort()
    suspicious_count=0
    sus_start_time=None
    end_time=None


    for i in range(len(timestamps)):
        start_time=timestamps[i]
        count=1


        for j in range(i+1,len(timestamps)):
            timediff=timestamps[j]-start_time

            if timediff<=timedelta(minutes=time_threshold):
                count+=1

            else:
                break

        if count>=failedlogin_threshold:
            sus_start_time=start_time
            end_time=timestamps[i+count-1]
            suspicious_count=count
            break

        
    if suspicious_count>=failedlogin_threshold:
        if suspicious_count>=10:
            severity="high"
        elif suspicious_count>=7:
            severity="alerting"
        else:
            severity="medium"

        alerts.append({
        "ip":ip_addresses,
        "login attempts":suspicious_count,
        "attack start time":sus_start_time,
        "Attack end time":end_time,
        "Severity level":severity

        })
        


# ---------------------------------------------- Display results --------------------------------------------------------------


print()
print("="*60)
print("SUSPICIOUS IP DETECTOR")
print("="*60)
print()

if not alerts:
    print("No suspicious activities detected")
else:
    print("Suspicious events detected",len(alerts))
    for i in alerts:
        print(f"[{i["Severity level"]}] Suspicious ip :{i["ip"]}")
        print(f"FAILED LOGINS:{i["login attempts"]}")
        print(f"Start time:{i["attack start time"]}")
        print(f"End time:{i["Attack end time"]}")
