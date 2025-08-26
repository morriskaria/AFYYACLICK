# AFYYACLICK
#SCREEN
1. Welcome Screen
    -> (L)ogin | (R)egister | (E)xit

2. Login Screen
    -> Enter Username:
    -> Enter Password:
    -> Redirect based on role (Admin, Doctor, Patient)

3. Patient Dashboard (after login)
    -> (B)ook Appointment
    -> (V)iew My Appointments
    -> (E)dit My Profile
    -> (L)ogout

4. Doctor Dashboard (after login)
    -> (V)iew My Appointments
        -> [List appointments] -> (S)elect one to add diagnosis/prescription
    -> (U)pdate Availability
    -> (L)ogout

5. Admin Dashboard (after login)
    -> (V)iew All Patients
    -> (V)iew All Doctors
    -> (A)dd New Doctor
    -> (L)ogout


# eHospital CLI Management System

A command-line interface (CLI) application for managing hospital operations, including patient records, doctor information, appointment scheduling, and medical records.

## Features

- **Patient Management**: Add, view, and search for patients
- **Doctor Management**: View doctors by specialization or ID
- **Appointment Scheduling**: Schedule, cancel, and complete appointments
- **Medical Records**: Add and view patient medical records

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd ehospital-cli