# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql://root:@localhost/crunchbase_2013', convert_unicode=True)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
Base = declarative_base()
Base.query = db_session.query_property()


class People(Base):
    __tablename__ = 'cb_people'
    id = Column(BigInteger, primary_key=True)
    object_id = Column(String(64), unique=True, key='object')
    first_name = Column(String(128))
    last_name = Column(String(128))
    birthplace = Column(String(128))
    affiliation_name = Column(String(128))


class Degrees(Base):
    __tablename__ = 'cb_degrees'
    id = Column(BigInteger, primary_key=True)
    object_id = Column(String(64), ForeignKey('cb_people.object'), key='person')
    degree_type = Column(String(32))
    subject = Column(String(255))
    institution = Column(String(64))
    graduated_at = Column(Date)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    cb_people = relationship(
        People,
        backref=backref(
            'cb_peoples',
            uselist=True,
            cascade='delete,all'
        )
    )
