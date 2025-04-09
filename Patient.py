class Patient:
    def __init__(self, fname, lname, age, n_room, diagnose):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.n_room=n_room
        self.diagnose = diagnose

    def info_patient(self):
        return f"({self.fname}, {self.lname}, {self.age}, {self.n_room}, {self.diagnose})"
    


def add_patient(patients_list, patient):
    patients_list.append(patient)

def search_name(patients_list):
    n = input("Eneter name: ")
    for patient in patients_list:
        if n==patient.fname:
            print(patient.info_patient())

def search_by_room(patients_list):
    m = int(input("Eneter number of room: "))
    for patient in patients_list:
        if m == patient.n_room:
            print(patient.info_patient())

def remove_patient(patients_list):
    l = input("Remove patient: ")
    for patient in patients_list:
        if l == patient.fname:
            patients_list.remove(patient)
            print(f"Patient {l} removed")
            break
    else:
        print(f"Patient {l} not found")

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter the number of patients: "))
            if num<1:
                raise ValueError("Invalid number...")
            else:
                break
        except ValueError as e:
            print(e)

patients_list = []
for i in range(num):
    patient_data = input(f"Patient {i+1}: ").split(',')
    patient = Patient(
        patient_data[0],
        patient_data[1],
        int(patient_data[2]),
        int(patient_data[3]),
        patient_data[4]
    )
    add_patient(patients_list,patient)

search_name(patients_list)
search_by_room(patients_list)
remove_patient(patients_list)

for patient in patients_list:
    print(patient.info_patient())
