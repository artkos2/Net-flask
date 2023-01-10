import atexit

from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PG_DSN = "postgresql+psycopg2://ads:secret@127.0.0.1:5431/ads"

engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)
# Base.metadata.drop_all()

class AdsModel(Base):

    __tablename__ = "ads2"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)
    create_date = Column(DateTime, server_default=func.now())


Base.metadata.create_all()

Session = sessionmaker(bind=engine)

atexit.register(lambda: engine.dispose())

#
# # @cached({})
# def get_engine():
#     return create_engine(config.PG_DSN)
#
#
# # @cached({})
# def get_session_maker():
#     return sessionmaker(bind=get_engine())
#
#
# def init_db():
#     Base.metadata.create_all(bind=get_engine())
#
#
# def close_db():
#     get_engine().dispose()
