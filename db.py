from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

user_name = "root"
user_pwd = "mysql"
db_host = "127.0.0.1"
db_name = "fastapi"

DATABASE = f'mysql://{user_name}:{user_pwd}@{db_host}/{db_name}?charset=utf8'

ENGINE = create_engine(
    DATABASE,
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()