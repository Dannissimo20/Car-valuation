import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()

PG_DSN = f'postgresql+psycopg2://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}'

Base = declarative_base()

class DBWriter:
    def __init__(self, db_url: str | None = None):
        self.engine = create_engine(
            db_url or PG_DSN,
            pool_size=20,
            max_overflow=20,
            pool_timeout=60
        )
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    @contextmanager
    def get_session(self):
        session: Session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            print(f"Session {session} rollback: {e}")
            session.rollback()
            raise
        finally:
            session.close()
