#data models 
# models.py
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(String)
    email = Column(String)
    
    appointments = relationship("Appointment", back_populates="patient")
    
    def __repr__(self):
        return f"Patient(id={self.id}, name='{self.first_name} {self.last_name}')"

class Doctor(Base):
    __tablename__ = 'doctors'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    specialization = Column(String)
    phone = Column(String)
    email = Column(String)
    
    appointments = relationship("Appointment", back_populates="doctor")
    
    def __repr__(self):
        return f"Doctor(id={self.id}, name='{self.first_name} {self.last_name}', specialization='{self.specialization}')"

class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    status = Column(String)
    date_time = Column(DateTime, default=datetime.now)  # Added datetime field
    
    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    
    def __repr__(self):
        return f"Appointment(id={self.id}, patient_id={self.patient_id}, doctor_id={self.doctor_id}, status='{self.status}')"
    

engine = create_engine('sqlite:///Afyyaclick.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
