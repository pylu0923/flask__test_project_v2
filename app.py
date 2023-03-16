from flask import Flask, render_template, jsonify, request
from database import load_from_db, load_job_from_db, add_application_to_db

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


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  # request.args contain information from the URL, 如果route method是post, info會存在
  # request.forms, 用成post是因為如果輸入欄位過多, URL會變成一大串, 用post就不會在URL後面
  # 接一串參數
  job = load_job_from_db(id)
  data = request.form
  add_application_to_db(id, data)
  # return request.args
  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
