from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'System Analyst',
        'location' : 'Hong Kong, China',
        'salary' : 'HKD 45,000'
        
    },
    {
        'id' : 2,
        'title' : 'Analyst  Programmer',
        'location' : 'London, England'
        
    },
    {
        'id' : 3,
        'title' : 'Sensior Analyst Programmer',
        'location' : 'Kowloon, Hong Kong',
        'salary' : 'HKD 35,000'
        
    },
    {
        'id' : 4,
        'title' : 'Programmer',
        'location' : 'Remote',
        'salary' : 'HKD 10,000'
        
    }
]


@app.route("/")
def hello_danny():
    return render_template("home.html", jobs=JOBS, compay_name = 'Danny')

#return JONS
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)



if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)
