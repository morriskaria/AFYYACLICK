# Import from models instead of creating a new engine
from db.models import get_db_session, Patient, Doctor, Appointment, MedicalRecord

def get_all_patients():
    session = get_db_session()
    try:
        return session.query(Patient).all()
    finally:
        session.close()

def get_patient_by_id(patient_id):
    session = get_db_session()
    try:
        return session.query(Patient).filter(Patient.id == patient_id).first()
    finally:
        session.close()

def add_patient(first_name, last_name, age, gender, phone, email, address):
    session = get_db_session()
    try:
        new_patient = Patient(
            first_name=first_name,
            last_name=last_name,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address
        )
        session.add(new_patient)
        session.commit()
        return new_patient
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_all_doctors():
    session = get_db_session()
    try:
        return session.query(Doctor).all()
    finally:
        session.close()

def get_doctor_by_id(doctor_id):
    session = get_db_session()
    try:
        return session.query(Doctor).filter(Doctor.id == doctor_id).first()
    finally:
        session.close()

def get_doctors_by_specialization(specialization):
    session = get_db_session()
    try:
        return session.query(Doctor).filter(Doctor.specialization == specialization).all()
    finally:
        session.close()

def schedule_appointment(patient_id, doctor_id, appointment_date, notes=""):
    session = get_db_session()
    try:
        new_appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            appointment_date=appointment_date,
            status="Scheduled",
            notes=notes
        )
        session.add(new_appointment)
        session.commit()
        return new_appointment
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_patient_appointments(patient_id):
    session = get_db_session()
    try:
        return session.query(Appointment).filter(Appointment.patient_id == patient_id).all()
    finally:
        session.close()

def get_doctor_appointments(doctor_id):
    session = get_db_session()
    try:
        return session.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()
    finally:
        session.close()

def add_medical_record(patient_id, diagnosis, treatment, prescription, doctor_notes):
    session = get_db_session()
    try:
        new_record = MedicalRecord(
            patient_id=patient_id,
            diagnosis=diagnosis,
            treatment=treatment,
            prescription=prescription,
            doctor_notes=doctor_notes
        )
        session.add(new_record)
        session.commit()
        return new_record
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_patient_medical_records(patient_id):
    session = get_db_session()
    try:
        return session.query(MedicalRecord).filter(MedicalRecord.patient_id == patient_id).all()
    finally:
        session.close()

def cancel_appointment(appointment_id):
    session = get_db_session()
    try:
        appointment = session.query(Appointment).filter(Appointment.id == appointment_id).first()
        if appointment:
            appointment.status = "Cancelled"
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def complete_appointment(appointment_id, notes=""):
    session = get_db_session()
    try:
        appointment = session.query(Appointment).filter(Appointment.id == appointment_id).first()
        if appointment:
            appointment.status = "Completed"
            appointment.notes = notes
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()