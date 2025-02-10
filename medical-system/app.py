from Patient import Patient
from MedicalRecord import VitalSign, LabResults, PhysicalExam


def main():
    print("Medical Clinic System\n")

    # SUBJECTIVE
    # Patient Basic Information
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")

    # Initialize Patient Instance
    patient = Patient(name, age, gender)

    # Patient Medical History
    history = input("Enter medical history (separate multiple entries with commas): ")
    symptom = input("Enter symptoms (separate multiple entries with commas): ")
    concern = input("Enter patient concerns: ")

    patient.add_medical_history(history)
    patient.add_symptom(symptom)
    patient.add_concern(concern)

    # OBJECTIVE
    # Vital Signs
    print("\nEnter Vital Signs:")
    blood_pressure = input("Blood Pressure (e.g., 120/80 mmHg): ")
    heart_rate = input("Heart Rate (bpm): ")
    temperature = input("Temperature (°C): ")

    vital_sign = VitalSign(blood_pressure, heart_rate, temperature)

    # Lab Results
    print("\nEnter Lab Results:")
    blood_test = input("Blood Test Results: ")
    urine_test = input("Urine Test Results: ")

    lab_result = LabResults(blood_test, urine_test)

    # Physical Examination
    print("\nEnter Physical Examination Findings:")
    general_appearance = input("General Appearance: ")
    heart_lungs = input("Heart and Lungs Condition: ")
    abdomen = input("Abdomen Condition: ")
    extremities = input("Extremities Condition: ")

    physical_exam = PhysicalExam(general_appearance, heart_lungs, abdomen, extremities)

    # Record to Patient
    patient.add_medical_record(vital_sign, lab_result, physical_exam)

    # ASSESSMENT
    patient.assess_patient()

    # Display Assessment
    print("\n--- Assessment ---")
    for i, assessment in enumerate(patient.assessment, 1):
        print(f"{i}. {assessment}")

    # PLAN
    patient.create_plan()

    # Ongoing Patient Care Loop
    while True:
        print("")
        print("\n--- Ongoing Patient Care ---")
        print("1. Add Treatment Plan")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            # Add Treatment Plan
            new_step = input("\nEnter a new treatment step: ")
            patient.treatment_plan.add_treatment_step(new_step)
            print("\nUpdated Treatment Plan:")
            patient.treatment_plan.display_plan()

        elif choice == "2":
            # Exit the loop
            print(
                "\nExiting the system. Thank you for using the Medical Clinic System!"
            )
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
