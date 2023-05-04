from sqlalchemy import create_engine
from sqlalchemy import text



db_connection_string = "mysql+pymysql://pscale_pw_nR14aQPsC4rEXC2xR8yRJiIeBo8puCs1yusMSC0CrSp@aws.connect.psdb.cloud/dannycareer?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print("Type(result): ", type(result))
    result_all = result.all()
    print("Type result_all(): ",type(result_all))
    first_result = result_all[0]
    print("type(first_result): ", type(first_result))
    