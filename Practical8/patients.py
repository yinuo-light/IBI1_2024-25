class patients:
# create a function to store individual's information
    def __init__(self, patient_name, age, date, medical_history):
        
        self.patient_name = patient_name
        self.age = age
        self.date = date
        self.medical_history = medical_history
# create a function to print the information
    def print_details(self):
# print the information in a line    
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, Date of Latest Admission: {self.date}, Medical History: {self.medical_history}")

# an example of how	the	function works
if __name__ == "__main__":
# create a patient
    patient1 = patients(
        patient_name="Zhang San",
        age=46,
        date="2025-04-08",
        medical_history="Flu"
    )

    patient1.print_details()