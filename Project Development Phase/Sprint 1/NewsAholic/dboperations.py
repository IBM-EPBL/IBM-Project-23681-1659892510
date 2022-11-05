import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30120;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xld66863;PWD=tDLqJWJNx98S9ftG","", "")
print("Connection Successful")
print(conn)

def signinuser():
    return "true"