from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
# import bycrypt

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()

# User class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    username = Column(String)
    password = Column(String)
    confirm_password = Column(String)
    tasks = relationship('Task', cascade = 'all, delete-orphan')

    def __init__(self, username, password, confirm_password):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

    def __repr__(self):
        return "<User(username='%s', password='%s', confirm_password='%s')>" % (self.username, self.password, self.confirm_password)


# Todo class
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key = True)
    title = Column(String)
    description = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    due_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id')) 

    def __init__(self, title, description, date_created, due_date, user_id):
        self.title = title
        self.description = description
        self.date_created = date_created
        self.due_date = due_date
        self.user_id = user_id
    def __repr__(self):
        return "<User(title='%s', description='%s', date_created='%s', due_date='%s')>" % (self.title, self.description, self.date_created, self.due_date)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
Session.configure(bind=engine)


