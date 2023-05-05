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
        #print(row._asdict())
        jobs.append(row._asdict())
    return jobs    
       
