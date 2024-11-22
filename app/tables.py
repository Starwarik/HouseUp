from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	name = Column(String, primary_key=True)
	password = Column(Integer)

class UserDevice(Base):
	__tablename__ = 'user_devices'
	id = Column(Integer, primary_key=True)
	user_name = Column(Integer, ForeignKey('users.name'))
	name = Column(String)
	type = Column(String)
	settings = Column(JSON)
	user = relationship('User', backref='user_devices')

class UserScenario(Base):
	__tablename__ = 'user_scenarios'
	id = Column(Integer, primary_key=True)
	user_name = Column(Integer, ForeignKey('users.name'))
	name = Column(String)
	content = Column(JSON)
	user = relationship('User', backref='user_scenarios')

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

