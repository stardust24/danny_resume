from sqlalchemy import create_engine
from sqlalchemy import text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']




# print(db_connection_string)

engine = create_engine(db_connection_string,
        connect_args={
        "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
        }
        })


#select data from database
#with engine.connect() as conn:
#    result = conn.execute(text("select * from jobs"))

 #   result_dicts = []
 #   for row in result.all():
 #       row_string = row
        # print out each row._asdict()
        #print(row._asdict())
  #      result_dicts.append(row._asdict())

        
def load_jobs_from_db():
    #select data from database
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        
    jobs = []
    for row in result.all():
        # row_string = row
        # print out each row._asdict()
        #print(row._asdict()) in dictionary format
        jobs.append(row._asdict())
    return jobs    

# select particular data from database with key
def retrieve_jobs_from_db(id):

#  with engine.connect() as conn:
#    result = conn.execute(text("select * from jobs where id = 1"))

    sql_string =  "select * from jobs where id = " + str(id)
    with engine.connect() as conn:
        result = conn.execute(text(sql_string))
    
#    with engine.connect() as conn:
#        result = conn.execute(text("select * form jobs where id = :val" ), val = id)

    
    result_all = result.all()
    if result_all == None:
        print("empty")
    else:
        row = result_all[0]._asdict()
        print("No empty")
        return row
        


#    if len(rows) == 0:
#        return None
#    else:
#        return rows[0]._asdict()
        
