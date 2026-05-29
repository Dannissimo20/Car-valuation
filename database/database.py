import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()

PG_DSN = os.getenv("PG_DSN")

Base = declarative_base()

class DBWriter:
    def __init__(self, db_url: str | None = None):
        self.engine = create_engine(db_url or PG_DSN)
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
