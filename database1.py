import sqlalchemy 
from sqlalchemy import create_engine, text
import os

#db_connection_string = "mysql+pymysql://username:password@host/schema?charset=utf8mb4"
db_connection_string = os.environ['DB_CONNECTION_STRING']

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

    if result_all == None:
        print("empty")
    else:
        print("No empty")


id = 1
with engine.connect() as conn:
    id = 1
    sql_string =  "select * from jobs where id = " + str(id)
    result = conn.execute(text(sql_string))

    print("tyep(result) : ",type(result))
    result_all = result.all()
    print("type(result_all) : ",type(result_all))
    #see the first element
    print(result_all[0]) 
    row = result_all[0]._asdict()
    print("particular result --")
    print("type(row) : ",type(row))
    print(row)