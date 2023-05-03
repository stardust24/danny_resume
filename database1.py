import sqlalchemy 

from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://kgb9j9gwoycojhxumyox:pscale_pw_S07W7uHzHBeTSjhrxUvWOq00xEAyVyJMb5Y4tKor84E@aws.connect.psdb.cloud/dannycareer?charset=utf8mb4"

engine = create_engine(db_connection_string,
        connect_args={
        "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
        }
        })

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())