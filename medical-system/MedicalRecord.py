class VitalSign:
    def __init__(self, blood_pressure, heart_rate, temperature):
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.temperature = temperature

    def display_vital_signs(self):
        print(f"Blood Pressure: {self.blood_pressure}")
        print(f"Heart Rate: {self.heart_rate} bpm")
        print(f"Temperature: {self.temperature}°C")


class LabResults:
    def __init__(self, blood_test, urine_test):
        self.blood_test = blood_test
        self.urine_test = urine_test

    def display_lab_results(self):
        print(f"Blood Test Results: {self.blood_test}")
        print(f"Urine Test Results: {self.urine_test}")


class PhysicalExam:
    def __init__(self, general_appearance, heart_lungs, abdomen, extremities):
        self.general_appearance = general_appearance
        self.heart_lungs = heart_lungs
        self.abdomen = abdomen
        self.extremities = extremities

    def display_physical_exam(self):
        print("Physical Examination Findings:")
        print(f"General Appearance: {self.general_appearance}")
        print(f"Heart and Lungs: {self.heart_lungs}")
        print(f"Abdomen: {self.abdomen}")
        print(f"Extremities: {self.extremities}")
