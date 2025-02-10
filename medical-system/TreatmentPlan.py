class TreatmentPlan:
    def __init__(self, patient):
        self.patient = patient
        self.treatment_steps = []

    def add_treatment_step(self, step):
        self.treatment_steps.append(step)

    def display_plan(self):
        print(f"Treatment Plan for {self.patient.name}:")
        for i, step in enumerate(self.treatment_steps, 1):
            print(f"{i}. {step}")
