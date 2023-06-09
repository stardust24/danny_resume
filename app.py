from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, retrieve_jobs_from_db, add_application_to_db
from database import load_work_exp, load_education, load_skill
from flask import request

from sqlalchemy import create_engine
from sqlalchemy import text


# call Flask
app = Flask(__name__)

# -----------------------------------------------------------------------
# append in domina name 
# extract data from database
@app.route("/", methods=['GET', 'POST'])
def hello_danny():
    exp_list = load_work_exp()
    edu_list = load_education()
    skill_list = load_skill() 
    return render_template("home.html", workexp = exp_list, edu = edu_list, skill = skill_list)

# -----------------------------------------------------------------------
#return about
@app.route("/about")
def show_about():
    return render_template('about.html')


#return contact
@app.route("/contact")
def show_contact():
    return render_template('contact.html')

#return link
@app.route("/link")
def show_link():
    return render_template('link.html')
# -----------------------------------------------------------------------
#return JONS
@app.route("/job/<id>")
def show_job(id):
    job_detail = retrieve_jobs_from_db(id)
    
# return null    
    if job_detail is None:
        return "Not Found", 404
    return render_template('jobpage.html',job = job_detail)
#   return jsonify(job_detail)

# -----------------------------------------------------------------------
# application form 
@app.route("/job/<id>/apply",methods=['post'])
def apply_to_job(id):
    data = request.form
    job_detail = retrieve_jobs_from_db(id) 
    #store arguement in DB
    add_application_to_db(id, data)
    #insert data from database
    return render_template('application_submitted.html',applcation = data, job = job_detail)
    
    
# -----------------------------------------------------------------------
# trun on Debug mode
if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)
