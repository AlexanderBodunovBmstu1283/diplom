# -*- coding: cp1251 -*-
import os
#os.startfile(r"c:/Python27/python.exe C:/Users/nick/PycharmProjects/mysql_pusher/push_PyQt.py")

import subprocess
string1="о_природе"
#with open("11.txt","r", encoding="utf8")as file:
#    for i in file:
#        string1=i
#string1=string1.encode("cp1251")
#print("Выводим в 1251\n")
#print (string1)
#print("Выводим as-is")
#print (string1)
#string1=string1.encode("utf8")
#print("Выводим в utf-8")
#print (string1)
proc = subprocess.Popen("c:/Python27/python.exe C:/Users/nick/PycharmProjects/mysql_pusher/push_PyQt.py nature", shell=True, stdout=subprocess.PIPE)
out = proc.stdout.readlines()