import random
import string
from datetime import date
import ibm_db
import json 
from flask import jsonify
from hashing import *
from newsapilocal import *

today = date.today()
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30120;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xld66863;PWD=tDLqJWJNx98S9ftG","", "")
print("Connection Successful")
print(conn)


def signinusersdb(name,password):
    stmt = ibm_db.exec_immediate(conn, "select user_key from adminusers where user_name='"+name+"';")
    while ibm_db.fetch_row(stmt) != False:
        value = ibm_db.result(stmt, 0)
        print(value)
        r = rehashing(value,password)
        return r
    return "Not found"

def signupusersdb(name,email,password):
    key = ''.join(random.choices(string.ascii_lowercase +string.digits, k=25))
    arr = hashing(password)
    stmt = "insert into adminusers (display_name, user_name, user_key, random_key) values ('"+name+"','"+ email+"','"+ str(arr.decode()) +"','"+ key+"' );"
    if ibm_db.exec_immediate(conn, stmt):
        return "Done"
    return "Error"

def storeheadlinesindb():
    a = getheadlines()
    d1 = today.strftime("%d/%m/%Y")
    val = '0'
    for i in a["articles"]:
        k = str(i).replace("None","'NA'")
        k = k.replace(",","U-001").replace('"',"U-002").replace("'","U-003")
        stmt = "insert into headlines (idate, headlinesdata) values ('"+d1+ "','" + k + "' );"
        if ibm_db.exec_immediate(conn, stmt):
            print("Stored")
    print("News stored to db")    
    return "Done"  

def getheadlinesfromdb():
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select hid,headlinesdata from headlines where idate='"+d1+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary 
  