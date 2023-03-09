from flask import Flask, render_template, jsonify
from database import load_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  JOBS = load_from_db()
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  JOBS = load_from_db()
  return jsonify(JOBS)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "not found", 404
  print(type(job))
  return render_template('jobpage.html', job=job)




if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
