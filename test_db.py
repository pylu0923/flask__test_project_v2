from sqlalchemy import create_engine, text
import os

db_connect_string = os.environ['DB_CONNECT_STRING']

engine = create_engine(db_connect_string, connect_args={
  "ssl" : {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

first = 'test_first'
last = 'test_last'
with engine.connect() as conn:
    conn.execute(
      text("insert into MyGuests (lastname, firstname) values ('{}','{}')".format(first, last))
    )
    # rows = result.all()  # result.all() == list

# print((rows[0]))