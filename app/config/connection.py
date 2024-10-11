from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

#Paranmetros para conexão de banco de dados Mysql.
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

#URL da conexão para o banco de dados Mysql.
DATABASE_URL =f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#conectando ao bando de dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session()
    try:  
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()