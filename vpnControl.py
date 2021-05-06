#!/usr/bin/env python





import os

os.system("apt-get install figlet")

os.system("clear")

os.system("figlet VPN CONTROL")





print("""

welcome 

""")







ip=input("target ip?")

os.system("ike-scan  "+ip)