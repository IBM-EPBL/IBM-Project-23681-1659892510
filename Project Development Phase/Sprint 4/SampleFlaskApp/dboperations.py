import random
import string
from datetime import date
import ibm_db
from flask import jsonify
from hashing import *
from newsapilocal import *

today = date.today()
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30120;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xld66863;PWD=tDLqJWJNx98S9ftG","", "")
print("Connection Successful")
print(conn)

def checkkey(id,key):
    stmt = ibm_db.exec_immediate(conn, "select random_key from adminusers where user_id='"+id+"';")
    while ibm_db.fetch_row(stmt) != False:
        value = ibm_db.result(stmt, 0)
        if(value == key):
            return '{"IsValid":"Done"}'
    return '{"IsValid":"No"}'

def signinusersdb(name,password):
    stmt = ibm_db.exec_immediate(conn, "select user_key,random_key,user_id,display_name from adminusers where user_name='"+name+"';")
    while ibm_db.fetch_row(stmt) != False:
        value = ibm_db.result(stmt, 0)
        key = ibm_db.result(stmt, 1)
        id = ibm_db.result(stmt, 2)
        dname = ibm_db.result(stmt,3)
        print(value)
        r = rehashing(value,password,key,id,dname)
        return r
    return '{"result":"Not Found"}'

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
    print(d1)
    for i in a["articles"]:
        k = str(i).replace("None","'NA'")
        k = k.replace(",","U-001").replace('"',"U-002").replace("'","U-003")
        stmt = "insert into headlines (idate, headlinesdata) values ('"+d1+ "','" + k + "' );"
        if ibm_db.exec_immediate(conn, stmt):
            print("Stored")
    b = getbusinessheadlines()
    for i in b["articles"]:
        k = str(i).replace("None","'NA'")
        k = k.replace(",","U-001").replace('"',"U-002").replace("'","U-003")
        stmt = "insert into business (idate, headlinesdata) values ('"+d1+ "','" + k + "' );"
        if ibm_db.exec_immediate(conn, stmt):
            print("Stored")
    c = getsportsheadlines();        
    for i in c["articles"]:
        k = str(i).replace("None","'NA'")
        k = k.replace(",","U-001").replace('"',"U-002").replace("'","U-003")
        stmt = "insert into sports (idate, headlinesdata) values ('"+d1+ "','" + k + "' );"
        if ibm_db.exec_immediate(conn, stmt):
            print("Stored")
    d = getentertainmentheadlines()
    for i in d["articles"]:
        k = str(i).replace("None","'NA'")
        k = k.replace(",","U-001").replace('"',"U-002").replace("'","U-003")
        stmt = "insert into entertainment (idate, headlinesdata) values ('"+d1+ "','" + k + "' );"
        if ibm_db.exec_immediate(conn, stmt):
            print("Stored")
    e = gettechheadlines()
    for i in e["articles"]:
        k = str(i).replace("None","'NA'")
        k = k.replace(",","U-001").replace('"',"U-002").replace("'","U-003")
        stmt = "insert into technology (idate, headlinesdata) values ('"+d1+ "','" + k + "' );"
        if ibm_db.exec_immediate(conn, stmt):
            print("Stored")
    f = gethealthheadlines()
    for i in f["articles"]:
        k = str(i).replace("None","'NA'")
        k = k.replace(",","U-001").replace('"',"U-002").replace("'","U-003")
        stmt = "insert into health (idate, headlinesdata) values ('"+d1+ "','" + k + "' );"
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

def getsingleheadlinedb(id):
    stmt = ibm_db.exec_immediate(conn, "select hid,headlinesdata from headlines where hid='"+str(id)+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary

def getbusinessheadlinesfromdb():
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select bid,headlinesdata from business where idate='"+d1+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary

def getsinglebusinessheadlinedb(id):
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select bid,headlinesdata from business where bid='"+str(id)+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary


def getsportsheadlinesfromdb():
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select sid,headlinesdata from sports where idate='"+d1+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary

def getsinglesportsheadlinedb(id):
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select sid,headlinesdata from sports where sid='"+str(id)+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary

def getentertainmentheadlinesfromdb():
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select eid,headlinesdata from ENTERTAINMENT where idate='"+d1+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary

def getsingleentertainmentheadlinedb(id):
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select eid,headlinesdata from ENTERTAINMENT where eid='"+str(id)+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary

def getsingletechheadlinedb(id):
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select tid,headlinesdata from technology where tid='"+str(id)+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary

def gettechheadlinesfromdb():
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select tid,headlinesdata from technology where idate='"+d1+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary 

def gethealthheadlinesfromdb():
    d1 = today.strftime("%d/%m/%Y")
    stmt = ibm_db.exec_immediate(conn, "select mid,headlinesdata from health where idate='"+d1+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary

def getsinglemedheadlinedb(id):
    stmt = ibm_db.exec_immediate(conn, "select mid,headlinesdata from health where mid='"+str(id)+"';")
    returndictionary = {}
    while ibm_db.fetch_row(stmt) != False:
        id =  ibm_db.result(stmt, 0)
        value = ibm_db.result(stmt, 1)
        print(id,value)
        print("Output")
        print(jsonify(str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")))
        returndictionary.update({id: str(value).replace("U-001",",").replace("U-002",'"').replace("U-003","'")})
    return returndictionary