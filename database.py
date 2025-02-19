from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})


SessinonLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base = declarative_base()

class Tickets(Base):
    __tablename__ = "tickets"
    id=Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    use = Column(String)
    price = Column(Integer)

Base.metadata.create_all(bind=engine)

async def get_db():
    db=SessinonLocal()
    try:
        yield db
    finally:
        db.close()




