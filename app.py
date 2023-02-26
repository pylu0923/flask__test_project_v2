from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Data Scientist',
    'location' : "Taipei",
    'salary' : '45,000'
  },
  {
    'id' : 2,
    'title' : 'Data Analyst',
    'location' : "HsinChu",
  },
  {
    'id' : 3,
    'title' : 'Frontend Engineer',
    'location' : "Taipei",
    'salary' : '45,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name = "PYLU")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

  
  
if __name__ == "__main__":
  app.run(host = '0.0.0.0' ,debug = True)