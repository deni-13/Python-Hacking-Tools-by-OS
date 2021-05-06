#!/usr/bin/env python

import os 
os.system("apt get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")

print("""Port taramaya hos geldin

1.hızlı tarama
2.servis ve versiyon
3.isletim sistemi

""")


islem_no=input("islem gir")


if (islem_no=="1"):
	hedefip=input("hedef ip ")	
	os.system("nmap "+ hedefip)
elif (islem_no=="2"):
	hedefip=input("hedef ip ")
	os.system("nmap -sS -sV" +hedefip)

elif (islem_no=="3"):
	hedefip=input("hedef ip  ")
	os.system("nmap -O "+hedefip)
	
else:
	print("hatalı")
