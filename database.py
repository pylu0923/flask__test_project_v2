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



db_connect_string = os.environ['DB_CONNECT_STRING']




engine = create_engine(db_connect_string, connect_args={
  "ssl" : {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})



# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))
#   result_all = result.all()# result.all() == list
#   result_dict_list = []
#   for row in result_all:
#     result_dict_list.append(row._asdict())# list內是row物件, 用._asdict可以轉成dict
