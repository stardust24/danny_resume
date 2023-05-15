from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, retrieve_jobs_from_db

# call Flask
app = Flask(__name__)

# append in domina name 
# extract data from database
@app.route("/")
def hello_danny():
    jobs_list = load_jobs_from_db()
    return render_template("home.html", jobs=jobs_list, compay_name = 'Danny')

#return JONS
@app.route("/job/<id>")
def show_job(id):
    job_detail = retrieve_jobs_from_db(id)
    if not job_detail:
        return "Not Found", 404
    return render_template('jobpage.html',job = job_detail)
#    return jsonify(job)

#@app.route("/api/jobs/<id>")
#def show_jobs(id):
#    job = load_jobs_from_db(id)
#    return jsonify(job)
    
# trun on Debug mode
if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)
