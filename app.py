from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

# call Flask
app = Flask(__name__)

@app.route("/")
def hello_danny():
    jobs_list = load_jobs_from_db()
    return render_template("home.html", jobs=jobs_list, compay_name = 'Danny')

#return JONS
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

# trun on Debug mode
if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)
