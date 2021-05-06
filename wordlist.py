#!/usr/bin/env python


import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet wordlist")


print("""
Wordlist OLusturuluyor......




""")


min_ch=input("minimum karakter sayısı?")
max_ch=input("maximum karakter sayısı?")
cha=input("karakter gir")


kayityeri=input("nereye kaydedilsin?")


os.system("crunch" + min_ch + " " + max_ch + " " + cha + "-o" + kayityeri)

print("ok")


#Eksiklikler var düzelticem!