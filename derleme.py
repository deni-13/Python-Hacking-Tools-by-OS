#!/usr/bin/env python



import os

import py_compile







os.system("apt-get install figlet")



os.system("clear")



os.system("figlet Compiler")





print("""

compiler started..



""")





compil=input("name of program----->")

	

py_compile.compile(compil)