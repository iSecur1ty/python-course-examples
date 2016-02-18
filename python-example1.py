#!/usr/bin/python

#This File is one of examples that used in iSecur1ty Pentesting with python course 
#http://www.isecur1ty.org/category/python-for-pentesters/


username = raw_input("Please Enter your Username : ")
password = raw_input("Please Enter your Password : ")

uname = "Admin"
password2  = "Admin123"

if username == uname and password == password2:
 print "Login Done !"
else:
 print "Please Enter your data again !"
