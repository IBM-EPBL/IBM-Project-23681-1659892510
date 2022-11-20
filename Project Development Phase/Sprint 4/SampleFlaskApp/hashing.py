import bcrypt
import os

def hashing(password):
    hash = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    print(hash)
    return hash
    

def rehashing(key,password_to_check,usrkey,id,name):
    if bcrypt.checkpw(password_to_check.encode('utf-8'),key.encode('utf-8')):
        return '{"result":"Found","key":"'+usrkey+'","userid":"'+str(id)+'","name":"'+name+'"}'
    else:
        return '{"result":"Not Found"}'    