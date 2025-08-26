# from models import Patient,Doctor,Appointment
# from faker import Faker#generate relistic fake data 
# import random#for random for varied data values 

# fake = Faker()

# specializations = [
#     "Cardiology", "Neurology", "Pediatrics", "Orthopedics", 
#     "Dermatology", "Psychiatry", "Oncology", "Radiology"
# ]

# def create_patients(session,count=10):
#     patients = []
#     for _ in range(count):
#         patient = Patient(
#             first_name=fake.first_name(),
#             last_name=fake.last_name(),
#             age=random.randint(18, 90),
#             gender=random.choice(['Male', 'Female']),
#             phone=fake.phone_number(),
#             email=fake.email(),
#             address=fake.address()
#         )
#         patients.append(patient)
#         session.add(patient)
#     session.commit()
#     return patients


# def create_doctors(session, count=8):
#     doctors = []
#     for i in range(count):
#         doctor = Doctor(
#             first_name=fake.first_name(),
#             last_name=fake.last_name(),
#             specialization=specializations[i % len(specializations)],
#             phone=fake.phone_number(),
#             email=fake.email(),
#             office_number=f"Room {100 + i}"
#         )
#         doctors.append(doctor)
#         session.add(doctor)
#     session.commit()
#     return doctors

# def create_appointments(session, patients, doctors, count=20):
#     statuses = ['Scheduled', 'Completed', 'Cancelled']
#     for _ in range(count):
#         appointment = Appointment(
#             patient_id=random.choice(patients).id,
#             doctor_id=random.choice(doctors).id,
#             appointment_date=fake.date_time_this_year(),
#             status=random.choice(statuses),
#             notes=fake.sentence()
#         )
#         session.add(appointment)
#     session.commit()

#     def seed_database():
#     print("Seeding database...")
    
#     # Create all tables first
#     create_tables()
    
#     # Get a database session
#     session = get_db_session()
    
#     try:
#         # Clear existing data
#         session.query(MedicalRecord).delete()
#         session.query(Appointment).delete()
#         session.query(Patient).delete()
#         session.query(Doctor).delete()
#         session.commit()
        
#         # Create new data
#         patients = create_patients(session)
#         doctors = create_doctors(session)
#         create_appointments(session, patients, doctors)
#         create_medical_records(session, patients)
        
#         print("Database seeded successfully!")
#     except Exception as e:
#         print(f"Error seeding database: {e}")
#         session.rollback()
#     finally:
#         session.close()

# if __name__ == "__main__":
#     seed_database()
