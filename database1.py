import sqlalchemy 

from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://1aqj44fdwrckuey2m4ex:pscale_pw_h8JgRmmXokkDC2vcDnfY09Z3EbOrSJMvQTeoFpLV9Oq@aws.connect.psdb.cloud/dannycareer?charset=utf8mb4"

engine = create_engine(db_connection_string,
        connect_args={
        "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
        }
        })

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print("tyep(result) : ",type(result))
 
    result_all = result.all()
    print("type(result_all) : ",type(result_all))
    #see the first element
    print(result_all[0]) 
    first_result = result_all[0]
    print("type(first_result) : ",type(first_result))



    
    