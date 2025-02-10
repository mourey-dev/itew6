from TreatmentPlan import TreatmentPlan


class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = []
        self.symptoms = []
        self.concern = ""
        self.medical_record = {}
        self.assessment = []  # Store assessment results
        self.treatment_plan = TreatmentPlan(self)  # Initialize TreatmentPlan

    def add_medical_history(self, history):
        histories = [s.strip() for s in history.split(",")]
        self.medical_history.extend(histories)

    def add_symptom(self, symptom):
        symptoms = [s.strip() for s in symptom.split(",")]
        self.symptoms.extend(symptoms)

    def add_concern(self, concern):
        self.concern = concern

    def add_medical_record(self, vital_sign, lab_result, physical_exam):
        self.medical_record = {
            "vital_sign": vital_sign,
            "lab_result": lab_result,
            "physical_exam": physical_exam,
        }

    def display_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}, Gender: {self.gender}")
        print("Medical History:", ", ".join(self.medical_history))
        print("Symptoms:", ", ".join(self.symptoms))
        print("Concern:", self.concern)

    def assess_patient(self):
        # Extract medical record data
        vital_sign = self.medical_record.get("vital_sign")
        lab_result = self.medical_record.get("lab_result")
        physical_exam = self.medical_record.get("physical_exam")

        # Clear previous assessment
        self.assessment = []

        # Check for hypertension
        if (
            "Hypertension" in self.medical_history
            and int(vital_sign.blood_pressure.split("/")[0]) >= 140
        ):
            self.assessment.append(
                "Hypertension detected. Monitor blood pressure and prescribe antihypertensive medication."
            )
            self.treatment_plan.add_treatment_step(
                "Prescribe antihypertensive medication."
            )
            self.treatment_plan.add_treatment_step(
                "Schedule a follow-up in 2 weeks to monitor blood pressure."
            )

        # Check for diabetes
        if (
            "Diabetes" in self.medical_history
            and "High glucose levels" in lab_result.blood_test
        ):
            self.assessment.append(
                "Diabetes detected. Adjust insulin therapy and recommend dietary changes."
            )
            self.treatment_plan.add_treatment_step("Adjust insulin therapy.")
            self.treatment_plan.add_treatment_step("Recommend dietary changes.")
            self.treatment_plan.add_treatment_step(
                "Schedule a blood glucose test in 1 month."
            )

        # Check for infection
        if "Fever" in self.symptoms and "Infection" in lab_result.urine_test:
            self.assessment.append(
                "Possible infection detected. Prescribe antibiotics and monitor symptoms."
            )
            self.treatment_plan.add_treatment_step("Prescribe antibiotics.")
            self.treatment_plan.add_treatment_step(
                "Monitor symptoms and schedule a follow-up in 1 week."
            )

        # Check for dehydration
        if (
            "Fatigue" in self.symptoms
            and "Dry mucous membranes" in physical_exam.general_appearance
        ):
            self.assessment.append(
                "Possible dehydration. Recommend increased fluid intake and monitor hydration status."
            )
            self.treatment_plan.add_treatment_step("Recommend increased fluid intake.")
            self.treatment_plan.add_treatment_step(
                "Monitor hydration status and schedule a follow-up in 1 week."
            )

        # Default assessment if no specific condition is detected
        if not self.assessment:
            self.assessment.append(
                "No specific condition detected. Further tests may be required."
            )
            self.treatment_plan.add_treatment_step("Schedule further diagnostic tests.")

    def create_plan(self):
        # Display the treatment plan
        self.treatment_plan.display_plan()
