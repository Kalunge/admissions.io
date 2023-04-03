from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///admissions.db', echo=True)

class Student(Base):

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    gpa = Column(String)
    sat = Column(String)
    act = Column(String)
    essay = Column(String)
    recommendations = Column(String)
    extracurriculars = Column(String)
    awards = Column(String)
    application_date = Column(String)
    status = Column(String)

    college_id = Column(Integer, ForeignKey('colleges.id'))

    college = relationship("College", backref=backref('students', order_by=id))

    def __init__(self, name, email, phone, address, city, state, zip, gpa, sat, act, essay, recommendations, extracurriculars, awards, application_date, status):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.gpa = gpa
        self.sat = sat
        self.act = act
        self.essay = essay
        self.recommendations = recommendations
        self.extracurriculars = extracurriculars
        self.awards = awards
        self.application_date = application_date
        self.status = status

    def __repr__(self):
        return '<Student %r>' % (self.name)

    def colleges(self):
        return self.colleges

    def admissions_applications(self):
        return self.admissions_applications

    def find_by_id(self, id):
        return self.query.filter_by(id=id).first()

class College(Base):

    __tablename__ = 'colleges'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    phone = Column(String)
    email = Column(String)
    website = Column(String)
    application_fee = Column(String)
    application_deadline = Column(String)
    application_status = Column(String)
    application_date = Column(String)
    
    students = relationship("Student", backref=backref('colleges', order_by=id))

    def __init__(self, name, address, city, state, zip, phone, email, website, application_fee, application_deadline, application_status, application_date, student):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email
        self.website = website
        self.application_fee = application_fee
        self.application_deadline = application_deadline
        self.application_status = application_status
        self.application_date = application_date
        self.student = student

    def __repr__(self):
        return '<College %r>' % (self.name)

      
    def students(self):
        return self.students



class AdmissionsApplication(Base):
  
      __tablename__ = 'admissions_applications'
  
      id = Column(Integer, primary_key=True)
      name = Column(String)
      address = Column(String)
      city = Column(String)
      state = Column(String)
      zip = Column(String)
      phone = Column(String)
      email = Column(String)
      website = Column(String)
      application_fee = Column(String)
      application_deadline = Column(String)
      application_status = Column(String)
      application_date = Column(String)
      student_id = Column(Integer, ForeignKey('students.id'))
      student = relationship("Student", backref=backref('admissions_applications', order_by=id))
  
      def __init__(self, name, address, city, state, zip, phone, email, website, application_fee, application_deadline, application_status, application_date, student):
          self.name = name
          self.address = address
          self.city = city
          self.state = state
          self.zip = zip
          self.phone = phone
          self.email = email
          self.website = website
          self.application_fee = application_fee
          self.application_deadline = application_deadline
          self.application_status = application_status
          self.application_date = application_date
          self.student = student
  
      def __repr__(self):
          return '<AdmissionsApplication %r>' % (self.name)
        
      def applications(self):
          return self.applications

      def students(self):
          return self.students

      def find_by_id(self, id):
          return self.query.filter_by(id=id).first()