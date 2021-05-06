#!/usr/bin/env pyhton

import os

os.system("apt-get install figlet")

os.system("clear")


os.system("figlet WORDPRESS SCANNER")


print("""

Loadiiiiiiinnnnngg.......

Welcome 



1-Fast Scan 
2-Cookie Scan
3-Theme Scan
4-Admin Username Scan



""")

ope=input("log the operation")

if ope=="1":
	site=input("site?")
	os.system("wpscan --url " + site)

if ope=="2":
	site=input("site?")
	os.system("wpscan --url " + site+  " --enumarate p")


if ope=="3":
	site=input("site?")
	os.system("wpscan --url " + site +  " --enumarate t")
	

if ope=="4":
	site=input("site?")
	os.system("wpscan --url " + site +  " --enumarate u")
	
else:
	print("invalid")
	
	




	


