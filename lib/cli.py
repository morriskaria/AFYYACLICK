from helpers import (
    get_all_patients, get_patient_by_id, add_patient,
    get_patient_appointments, get_patient_medical_records, 
)
from db.models import get_db_session
def display_patient_menu():
    """Display the patient management menu"""
    print("\n--- Patient Management ---")
    print("1. View All Patients")
    print("2. Search Patient by ID")
    print("3. Add New Patient")
    print("4. View Patient Appointments")
    print("5. View Patient Medical Records")
    print("6. Back to Main Menu")
    
    choice = input("Please select an option (1-6): ")
    return choice

def view_all_patients():
    """Display all patients in the system"""
    patients = get_all_patients()
    if patients:
        print("\nAll Patients:")
        print("-" * 80)
        for patient in patients:
            print(f"ID: {patient.id} | Name: {patient.first_name} {patient.last_name} | "
                  f"Age: {patient.age} | Gender: {patient.gender} | Phone: {patient.phone}")
        print("-" * 80)
    else:
        print("No patients found in the system.")

def search_patient_by_id():
    """Search for a patient by their ID"""
    try:
        patient_id = int(input("Enter patient ID: "))
        patient = get_patient_by_id(patient_id)
        
        if patient:
            print(f"\nPatient Details:")
            print(f"ID: {patient.id}")
            print(f"Name: {patient.first_name} {patient.last_name}")
            print(f"Age: {patient.age}")
            print(f"Gender: {patient.gender}")
            print(f"Phone: {patient.phone}")
            print(f"Email: {patient.email}")
            print(f"Address: {patient.address}")
            print(f"Registered: {patient.created_at}")
        else:
            print("Patient not found!")
    except ValueError:
        print("Please enter a valid numeric ID!")

def add_new_patient():
    """Add a new patient to the system"""
    print("\nAdd New Patient:")
    print("Please enter the following details:")
    
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    age = input("Age: ").strip()
    gender = input("Gender (Male/Female/Other): ").strip().capitalize()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    
    # Validate required fields
    if not all([first_name, last_name, age, gender, phone]):
        print("Error: First Name, Last Name, Age, Gender, and Phone are required!")
        return
    
    try:
        age = int(age)
        if age <= 0:
            print("Age must be a positive number!")
            return
            
        new_patient = add_patient(first_name, last_name, age, gender, phone, email, address)
        print(f"Patient added successfully! ID: {new_patient.id}")
    except ValueError:
        print("Age must be a valid number!")

def view_patient_appointments():
    """View appointments for a specific patient"""
    try:
        patient_id = int(input("Enter patient ID: "))
        appointments = get_patient_appointments(patient_id)
        
        if appointments:
            print(f"\nAppointments for Patient ID {patient_id}:")
            print("-" * 80)
            for appt in appointments:
                print(f"Appointment {appt.id}: Dr. {appt.doctor.last_name} on "
                      f"{appt.appointment_date} - Status: {appt.status}")
                if appt.notes:
                    print(f"  Notes: {appt.notes}")
            print("-" * 80)
        else:
            print("No appointments found for this patient!")
    except ValueError:
        print("Please enter a valid numeric ID!")

def view_patient_medical_records():
    """View medical records for a specific patient"""
    try:
        patient_id = int(input("Enter patient ID: "))
        records = get_patient_medical_records(patient_id)
        
        if records:
            print(f"\nMedical Records for Patient ID {patient_id}:")
            print("=" * 80)
            for record in records:
                print(f"Record ID: {record.id}")
                print(f"Date: {record.visit_date}")
                print(f"Diagnosis: {record.diagnosis}")
                print(f"Treatment: {record.treatment}")
                print(f"Prescription: {record.prescription}")
                if record.doctor_notes:
                    print(f"Doctor Notes: {record.doctor_notes}")
                print("-" * 40)
        else:
            print("No medical records found for this patient!")
    except ValueError:
        print("Please enter a valid numeric ID!")

def patient_management():
    """Main patient management function"""
    while True:
        choice = display_patient_menu()
        
        if choice == "1":
            view_all_patients()
        elif choice == "2":
            search_patient_by_id()
        elif choice == "3":
            add_new_patient()
        elif choice == "4":
            view_patient_appointments()
        elif choice == "5":
            view_patient_medical_records()
        elif choice == "6":
            break
        else:
            print("Invalid option! Please try again.")