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

# -----------------------------------------------------------------------
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

# -----------------------------------------------------------------------
# select particular data from database with key
def retrieve_jobs_from_db(id):

#  with engine.connect() as conn:
#    result = conn.execute(text("select * from jobs where id = 1"))

    sql_string =  "select * from jobs where id = " + str(id)
    with engine.connect() as conn:
        result = conn.execute(text(sql_string))
    
#    with engine.connect() as conn:
#        result = conn.execute(text("select * form jobs where id = :val" ), val = id)
    
#    result_all = result.all()
    result_all = result.fetchall()
    if len(result_all):
        print("reuslt is not None!")
        row = result_all[0]._asdict()
        return row
    else:
        return None

# -----------------------------------------------------------------------
#store arguement in DB
def add_application_to_db(id, data):

    sql_str = "insert into applications  (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) values ( "
    sql_str = sql_str + id + ", '"+  data['full_name'] + "', '"+  data['email'] + "',  '"+ data['linkedin_url'] + "', '"
    sql_str = sql_str + data['education']+ "', '" + data['work_experience']+ "', '" +  data['resume_url'] + "')"

    print(sql_str)
    
    with engine.connect() as conn:
        conn.execute(text(sql_str))    
    
    #insert data from database

