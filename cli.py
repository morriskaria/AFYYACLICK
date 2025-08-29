#import
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Patient, Doctor, Appointment
import sys

class Afyyaclick:
    def __init__(self):
        self.engine = create_engine("sqlite:///Afyyaclick.db")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def welcome(self):
        print("""
        
                 ==WELCOME TO AFYYACLICK==      
           ==Your Personal Health Companion==   
        """)

#display menu 
    def display_menu(self):
        print("1. View all patients")
        print("2. View all doctors")
        print("3. View all appointments")
        print("4. Add new patient")
        print("5. Add new doctor")
        print("6. Schedule appointment")
        print("7. Exit")

#loops
    def run(self):
         self.welcome()
         while True:
             self.display_menu()
             choice = input("Enter your choice (1-7): ")
        
             if choice == "1":
                 self.view_patients()
             elif choice == "2":
                 self.view_doctors()
             elif choice == "3":
                 self.view_appointments()
             elif choice == "4":
                 self.add_patient()
             elif choice == "5":
                 self.add_doctor()
             elif choice == "6":
                 self.schedule_appointment()
             elif choice == "7":
                print("bye:)!")
                sys.exit()
             else:
                print("Invalid choice. Please try again.")


#view patients
    def view_patients(self):
          patients = self.session.query(Patient).all()
          print("\n=== Patients ===")
          for patient in patients:
              print(f"{patient.id}: {patient.first_name} {patient.last_name}, {patient.age}, {patient.gender}")

    def view_doctors(self):
        doctors = self.session.query(Doctor).all()
        print("\n=== Doctors ===")
        for doctor in doctors:
            print(f"{doctor.id}: Dr. {doctor.first_name} {doctor.last_name}, {doctor.specialization}")
    
    def view_appointments(self):
        appointments = self.session.query(Appointment).all()
        print("\n=== Appointments ===")
        for appointment in appointments:
            patient = self.session.query(Patient).filter_by(id=appointment.patient_id).first()
            doctor = self.session.query(Doctor).filter_by(id=appointment.doctor_id).first()
            print(f"{appointment.id}: {patient.first_name} {patient.last_name} with Dr. {doctor.first_name} {doctor.last_name} - {appointment.status}")
    

#adding new patient 
    def add_patient(self):
        print("\n=== Add New Patient ===")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        phone = input("Phone: ")
        email = input("Email: ")
        
        new_patient = Patient(
            first_name=first_name,
            last_name=last_name,
            age=age,
            gender=gender,
            phone=phone,
            email=email
        )
        
        self.session.add(new_patient)
        self.session.commit()
        print("Patient added successfully!")



    def add_doctor(self):
        print("\n=== Add New Doctor ===")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        specialization = input("Specialization: ")
        phone = input("Phone: ")
        email = input("Email: ")
        
        new_doctor = Doctor(
            first_name=first_name,
            last_name=last_name,
            specialization=specialization,
            phone=phone,
            email=email
        )
        
        self.session.add(new_doctor)
        self.session.commit()
        print("Doctor added successfully!")


#appointments 
    def schedule_appointment(self):
        print("\n=== Schedule Appointment ===")


#display all the doctors
        patients = self.session.query(Patient).all()
        print("Patients:")
        for patient in patients:
            print(f"{patient.id}: {patient.first_name} {patient.last_name}")
        
        patient_id = int(input("Select patient ID: "))
        
        # Show available doctors
        doctors = self.session.query(Doctor).all()
        print("Doctors:")
        for doctor in doctors:
            print(f"{doctor.id}: Dr. {doctor.first_name} {doctor.last_name} ({doctor.specialization})")
        
        doctor_id = int(input("Select doctor ID: "))
        status = input("Status (Scheduled/Completed/Cancelled): ")
        
        new_appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            status=status
        )
        
        self.session.add(new_appointment)
        self.session.commit()
        print("Appointment scheduled successfully!")

if __name__ == "__main__":
    cli = Afyyaclick()
    cli.run()