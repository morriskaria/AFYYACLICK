#seeding data to my database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Patient, Doctor, Appointment
from datetime import datetime, timedelta

#main seeding function
def seed_database():
    pass