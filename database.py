from sqlalchemy import create_engine
from sqlalchemy import text




# db_connection_string = "mysql+pymysql://1aqj44fdwrckuey2m4ex:pscale_pw_h8JgRmmXokkDC2vcDnfY09Z3EbOrSJMvQTeoFpLV9Oq@aws.connect.psdb.cloud/dannycareer?charset=utf8mb4"


user_name = "1aqj44fdwrckuey2m4ex"
pass_string = "pscale_pw_h8JgRmmXokkDC2vcDnfY09Z3EbOrSJMvQTeoFpLV9Oq"
hostname_string = "aws.connect.psdb.cloud"
dbname_string = "dannycareer"
db_connection_string = "mysql+pymysql://" + user_name + ":" + pass_string + "@" + hostname_string +"/" + dbname_string + "?charset=utf8mb4"

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
       
