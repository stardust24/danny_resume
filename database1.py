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

#sl_str ="select person_exp_hist.resume_id, person_exp_hist.profile_id, person_exp_hist.working_date_from, person_exp_hist.working_date_end, person_exp_hist.job_title, person_exp_hist.company_name, person_exp_hist.location, person_exp_hist.responsibilities, person_profile.name, person_profile.last_name, person_profile.achievements FROM  person_exp_hist JOIN person_profile ON person_exp_hist.profile_id = person_profile.profile_id"


sl_str = "SELECT person_profile.name, person_profile.last_name, person_education.education FROM person_education INNER JOIN person_profile ON person_profile.profile_id = person_education.profile_id "

with engine.connect() as conn:
  result = conn.execute(text(sl_str))
        
education = []
for row in result.all():
        # row_string = row
        # print out each row._asdict()
        #print(row._asdict()) in dictionary format
    education.append(row._asdict())


print(list(education))

for row in education:
    print(row)



#for item in education:
#  if item['resume_id'] == 1:
#      for line in item['responsibilities']. splitlines():
#          print(line)
#      print(' ')