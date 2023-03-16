from sqlalchemy import create_engine, text
import os


def load_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()  # result.all() == list
    result_dict_list = []
    for row in result_all:
      result_dict_list.append(row._asdict())  # list內是row物件, 用._asdict可以轉成dict
  return result_dict_list


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
    rows = result.all()  # result.all() == list
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()  # list內是row物件, 用._asdict可以轉成dict


def create_table(table_name):
  table_list = []
  with engine.connect() as conn:
    result = conn.execute(text("SHOW tables"))
    for x in result:
      table_list.append(x[0])
    if not table_name in table_list:
      print("now creating table....please wait")
      sql = f"CREATE TABLE {table_name} (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, job_id INT NOT NULL, full_name VARCHAR(255) NOT NULL,\
           email VARCHAR(255) NOT NULL, linkedin VARCHAR(500), education VARCHAR(2000), work_experience VARCHAR(2000))"
      
      conn.execute(text(sql))


def add_application_to_db(job_id, data):
  table_name = 'applications'
  create_table(table_name)
  # insert into後面的value用f-string要再用''包起來
  with engine.connect() as conn:
    query = text(
      f"insert into {table_name} (job_id, full_name, email, linkedin,\
    education, work_experience) VALUES ('{job_id}', '{data['full_name']}',' {data['email']}', '{data['linkedin']}','{data['education']}', '{data['work_experience']}')")
    conn.execute(query)


db_connect_string = os.environ['DB_CONNECT_STRING']

engine = create_engine(db_connect_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))
#   result_all = result.all()# result.all() == list
#   result_dict_list = []
#   for row in result_all:
#     result_dict_list.append(row._asdict())# list內是row物件, 用._asdict可以轉成dict
