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

# --------------load work experience ---------------------------------------------------------
def load_work_exp():
    #select data from database
    sl_str ="select person_exp_hist.resume_id, person_exp_hist.profile_id, person_exp_hist.working_date_from, person_exp_hist.working_date_end, person_exp_hist.job_title, person_exp_hist.company_name, person_exp_hist.location, person_exp_hist.responsibilities, person_profile.name, person_profile.last_name, person_profile.date_of_birth, person_profile.phone, person_profile.email, person_profile.interests, person_profile.achievements FROM  person_exp_hist JOIN person_profile ON person_exp_hist.profile_id = person_profile.profile_id order by person_exp_hist.working_date_from DESC"
  
    with engine.connect() as conn:
        result = conn.execute(text(sl_str))
        
    experience = []
    for row in result.all():
        # row_string = row
        # print out each row._asdict()
        #print(row._asdict()) in dictionary format
        experience.append(row._asdict())
    return experience    


# --------------load education ------------------------------------
def load_education():
    #select data from database
    sl_str = "SELECT person_profile.name, person_profile.last_name, person_education.education FROM person_education INNER JOIN person_profile ON person_profile.profile_id = person_education.profile_id "
  
    with engine.connect() as conn:
        result = conn.execute(text(sl_str))
        
    education = []
    for row in result.all():
        # row_string = row
        # print out each row._asdict()
        #print(row._asdict()) in dictionary format
        education.append(row._asdict())
    return education


# --------------load skill ------------------------------------
def load_skill():
    #select data from database
    sl_str = "SELECT person_profile.name, person_profile.last_name, person_skill.skill_name, person_skill.years_of_experience FROM  person_skill INNER JOIN person_profile ON person_profile.profile_id = person_skill.profile_id order by person_skill.skill_name ASC"
  
    with engine.connect() as conn:
        result = conn.execute(text(sl_str))
        
    skill = []
    for row in result.all():
        # row_string = row
        # print out each row._asdict()
        #print(row._asdict()) in dictionary format
        skill.append(row._asdict())
    return skill

# -----------------------------------------------------------------------        
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

