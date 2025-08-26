from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker



#create an engine for my db 
my_engine = create_engine("sqlite:///ehospital.db")

#making a my_session 
session_config = sessionmaker(bind=my_engine)

my_session = session_config()

#add a base.meta data


#our classes need to inherit from adeclarative base object 
Base = declarative_base()


class Patient(Base):
    __tablename__ = 'patients'

#class Attributes for my table that represent my table Coulmns 

    id = Column(Integer, primary_key=True)#unique identifier for every table 
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(String)
    email = Column(String)


def __repr__(self):
    return f"Patient(id={self.id}, name='{self.first_name} {self.last_name}')"


class Doctor(Base):
    #intialize our table name 
    __tablename__ = 'doctors'

    #class Attributes for my table that represent my table Coulmns 


    id = Column(Integer, primary_key=True)#unique identifier for every table 
    first_name = Column(String)
    last_name = Column(String)
    specialization = Column(String)
    phone = Column(String)
    email = Column(String)

    
    def __repr__(self):
        return f"Doctor(id={self.id}, name='{self.first_name} {self.last_name}', specialization='{self.specialization}')"
    



class Appointments(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key =True)#unique identifier for every table 
    patient_id = Column(Integer,ForeignKey('patients.id'))
    doctor_id = Column(Integer,ForeignKey('doctors.id'))
    status = Column(String)

    def __repr__(self):
        return f"Appointment(id={self.id}, patient_id={self.patient_id}, doctor_id={self.doctor_id}, status='{self.status}')"
    


#call base.meta data to my engine
Base.metadata.create_all(my_engine)

#create some data to my table 
#1.accses the session 


# doctor1 = Doctor(first_name="Mourice", last_name="Karia", specialization="surgeon", phone="0115752629", email="morriskaria542@gmail.com")
# my_session.add(doctor1)
# my_session.commit()


if __name__ == '__main__':
 doctors = [
    Doctor(
        first_name="Sarah",
        last_name="Johnson",
        specialization="Cardiologist",
        phone="0721555666",
        email="sarah.johnson@hospital.com"
    ),
    Doctor(
        first_name="Michael",
        last_name="Chen",
        specialization="Neurologist",
        phone="0731777888",
        email="michael.chen@neuroclinic.com"
    ),
    Doctor(
        first_name="Amina",
        last_name="Patel",
        specialization="Pediatrician",
        phone="0741999000",
        email="amina.patel@childrenshospital.com"
    ),
    Doctor(
        first_name="David",
        last_name="Williams",
        specialization="Orthopedic Surgeon",
        phone="0751222333",
        email="david.williams@orthocare.com"
    ),
    Doctor(
        first_name="Lisa",
        last_name="Rodriguez",
        specialization="Dermatologist",
        phone="0761444555",
        email="lisa.rodriguez@skinclinic.com"
    ),
    Doctor(
        first_name="James",
        last_name="Taylor",
        specialization="Ophthalmologist",
        phone="0771666777",
        email="james.taylor@eyecenter.com"
    ),
    Doctor(
        first_name="Emily",
        last_name="Wilson",
        specialization="Gynecologist",
        phone="0781888999",
        email="emily.wilson@womenshealth.com"
    ),
    Doctor(
        first_name="Robert",
        last_name="Kim",
        specialization="Psychiatrist",
        phone="0791111222",
        email="robert.kim@mentalhealth.com"
    ),
    Doctor(
        first_name="Maria",
        last_name="Garcia",
        specialization="Dentist",
        phone="0701333444",
        email="maria.garcia@dentalcare.com"
    ),
    Doctor(
        first_name="Thomas",
        last_name="Brown",
        specialization="General Practitioner",
        phone="0711555666",
        email="thomas.brown@familyclinic.com"
    )
]

# my_session.add_all(doctors)
# my_session.commit()
#sessions-it a working copy of my db that helps making changing in my db 

# Create some patient instances
patients = [
    Patient(
        first_name="John",
        last_name="Smith",
        age=35,
        gender="Male",
        phone="0720111222",
        email="john.smith@email.com"
    ),
    Patient(
        first_name="Mary",
        last_name="Johnson",
        age=28,
        gender="Female",
        phone="0721333444",
        email="mary.johnson@email.com"
    ),
    Patient(
        first_name="Daniel",
        last_name="Kimani",
        age=42,
        gender="Male",
        phone="0721555666",
        email="daniel.kimani@email.com"
    ),
    Patient(
        first_name="Grace",
        last_name="Mwangi",
        age=31,
        gender="Female",
        phone="0721777888",
        email="grace.mwangi@email.com"
    ),
    Patient(
        first_name="Paul",
        last_name="Ochieng",
        age=19,
        gender="Male",
        phone="0721999000",
        email="paul.ochieng@email.com"
    ),
    Patient(
        first_name="Susan",
        last_name="Atieno",
        age=65,
        gender="Female",
        phone="0721111333",
        email="susan.atieno@email.com"
    ),
    Patient(
        first_name="Brian",
        last_name="Odhiambo",
        age=8,
        gender="Male",
        phone="0721222444",
        email="brian.odhiambo@email.com"
    ),
    Patient(
        first_name="Lucy",
        last_name="Wanjiku",
        age=24,
        gender="Female",
        phone="0721333555",
        email="lucy.wanjiku@email.com"
    ),
    Patient(
        first_name="Peter",
        last_name="Kamau",
        age=51,
        gender="Male",
        phone="0721444666",
        email="peter.kamau@email.com"
    ),
    Patient(
        first_name="Esther",
        last_name="Nyambura",
        age=37,
        gender="Female",
        phone="0721555777",
        email="esther.nyambura@email.com"
    ),
    Patient(
        first_name="David",
        last_name="Mbugua",
        age=29,
        gender="Male",
        phone="0721666888",
        email="david.mbugua@email.com"
    ),
    Patient(
        first_name="Ruth",
        last_name="Wairimu",
        age=22,
        gender="Female",
        phone="0721777999",
        email="ruth.wairimu@email.com"
    ),
    Patient(
        first_name="Joseph",
        last_name="Ndirangu",
        age=45,
        gender="Male",
        phone="0721888000",
        email="joseph.ndirangu@email.com"
    ),
    Patient(
        first_name="Sarah",
        last_name="Adhiambo",
        age=33,
        gender="Female",
        phone="0721999111",
        email="sarah.adhiambo@email.com"
    ),
    Patient(
        first_name="Samuel",
        last_name="Gitonga",
        age=17,
        gender="Male",
        phone="0721000222",
        email="samuel.gitonga@email.com"
    )
]




# all_patients = my_session.query(Doctor).all()
# print(all_patients)



    
# Add to session and commit
my_session.add_all(patients)
my_session.commit()


# Create some appointment instances
appointments = [
    Appointments(
        patient_id=1,  # John Smith
        doctor_id=1,   # Sarah Johnson (Cardiologist)
        status="Scheduled"
    ),
    Appointments(
        patient_id=2,  # Mary Johnson
        doctor_id=3,   # Amina Patel (Pediatrician)
        status="Completed"
    ),
    Appointments(
        patient_id=3,  # Daniel Kimani
        doctor_id=2,   # Michael Chen (Neurologist)
        status="Scheduled"
    ),
    Appointments(
        patient_id=4,  # Grace Mwangi
        doctor_id=7,   # Emily Wilson (Gynecologist)
        status="Completed"
    ),
    Appointments(
        patient_id=5,  # Paul Ochieng
        doctor_id=3,   # Amina Patel (Pediatrician)
        status="Cancelled"
    ),
    Appointments(
        patient_id=6,  # Susan Atieno
        doctor_id=1,   # Sarah Johnson (Cardiologist)
        status="Scheduled"
    ),
    Appointments(
        patient_id=7,  # Brian Odhiambo
        doctor_id=3,   # Amina Patel (Pediatrician)
        status="Completed"
    ),
    Appointments(
        patient_id=8,  # Lucy Wanjiku
        doctor_id=9,   # Maria Garcia (Dentist)
        status="Scheduled"
    ),
    Appointments(
        patient_id=9,  # Peter Kamau
        doctor_id=4,   # David Williams (Orthopedic Surgeon)
        status="Completed"
    ),
    Appointments(
        patient_id=10, # Esther Nyambura
        doctor_id=5,   # Lisa Rodriguez (Dermatologist)
        status="Scheduled"
    ),
    Appointments(
        patient_id=11, # David Mbugua
        doctor_id=6,   # James Taylor (Ophthalmologist)
        status="Completed"
    ),
    Appointments(
        patient_id=12, # Ruth Wairimu
        doctor_id=7,   # Emily Wilson (Gynecologist)
        status="Scheduled"
    ),
    Appointments(
        patient_id=13, # Joseph Ndirangu
        doctor_id=8,   # Robert Kim (Psychiatrist)
        status="Completed"
    ),
    Appointments(
        patient_id=14, # Sarah Adhiambo
        doctor_id=10,  # Thomas Brown (General Practitioner)
        status="Scheduled"
    ),
    Appointments(
        patient_id=15, # Samuel Gitonga
        doctor_id=3,   # Amina Patel (Pediatrician)
        status="Cancelled"
    ),
    Appointments(
        patient_id=1,  # John Smith
        doctor_id=10,  # Thomas Brown (General Practitioner)
        status="Scheduled"
    ),
    Appointments(
        patient_id=3,  # Daniel Kimani
        doctor_id=8,   # Robert Kim (Psychiatrist)
        status="Completed"
    ),
    Appointments(
        patient_id=6,  # Susan Atieno
        doctor_id=2,   # Michael Chen (Neurologist)
        status="Scheduled"
    ),
    Appointments(
        patient_id=9,  # Peter Kamau
        doctor_id=1,   # Sarah Johnson (Cardiologist)
        status="Completed"
    )
]

# Add to session and commit
my_session.add_all(appointments)
my_session.commit()




