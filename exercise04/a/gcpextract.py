import os

from google.cloud.sql.connector import Connector, IPTypes
import pg8000

import sqlalchemy

def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    """
    Initializes a connection pool for a Cloud SQL instance of Postgres.

    Uses the Cloud SQL Python Connector package.
    """
    instance_connection_name = os.environ["INSTANCE_CONNECTION_NAME"]  # e.g. 'project:region:instance'
    db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
    db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
    db_name = os.environ["DB_NAME"]  # e.g. 'my-database'

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    # initialize Cloud SQL Python Connector object
    connector = Connector()

    def getconn() -> pg8000.dbapi.Connection:
        conn: pg8000.dbapi.Connection = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
            ip_type=ip_type,
        )
        return conn

    # The Cloud SQL Python Connector can be used with SQLAlchemy
    # using the 'creator' argument to 'create_engine'
    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
        # ...
    )
    return pool


def call_db(pool):
    with pool.connect() as db_conn:
        result1 = db_conn.execute(sqlalchemy.text("SELECT * from activity.sms_record limit 1000")).fetchall()
        result2 = db_conn.execute(sqlalchemy.text("SELECT * from activity.mobile_data_activity limit 1000")).fetchall()
        return result1, result2

def main():
    pool = connect_with_connector()
    r1, r2 = call_db(pool)
    print(r1)
    print(r2)


if __name__ == '__main__':
    main()