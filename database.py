from sqlalchemy import create_engine, text 


db_connection_string = "mysql+pymysql://2gjqqg3wukepi9pgxcs5:pscale_pw_6Jbv3f0S4U7NozKFskpYLvagyjkUP3cQQATcOYBLtl1@aws.connect.psdb.cloud/dannycareer?charset=utf8mb4"

engine = create_engine(
    db_connection_string, 
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    }
)


with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(type(result))
    result_all = result.all()
    print(type(result_all))