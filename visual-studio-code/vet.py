patients = {
    123:{
        "name":"Alvin",
        "type":"Cat",
        "age":10
    },
    1234:{
        "name":"Alex",
        "type":"Dog",
        "age":4
    }
}

def add_pet():
    patient_id = 0
    patient_type = ""
    patient_age = -1
    patient_name = ""

    allowed_types = ["cat", "dog", "turtle", "bird"]

    while True:
        try:
            patient_id = int(input("Enter the patient number:"))
            if patient_id in patients:
                print("You cant use this number!")
                continue
            else:
                break
        except:
            print("Patient id must be a number")
    
    while patient_name == "":
        patient_name = input("Enter the name:")
        if patient_name.replace(" ", "") == "":
            print("Seriously? You cant use all spaces")
    
    while patient_type not in allowed_types:
        patient_type = input("Enter the patient type:").lower()
    
    while patient_age < 0:
        try:
            patient_age = int(input("Enter the patient age:"))
        except:
            print("Age must be a digit")
    
    patients[patient_id] = {
        "name":patient_name,
        "age":patient_age,
        "type":patient_type
    }
    print("Patient was successfully added to the list")

def view_all_pets():
    if len(patients) == 0:
        print("No patients to show")

    for patient in patients:
        print(patients[patient]["name"])

def view_all_data():
    if len(patients) == 0:
        print("No patients to show")

    for patient in patients:
        """"
        id = patient
        patient = patients[patient]
        name = patient["name"]
        age = patient["age"]
        type = patient["type"]
        print(f"id:{id},name:{name}, age:{age}, type:{type}")
        """
        for patient in patients:
            for key,value in patients[patient].items():
                print(f"{key}:{value}")
            print("\n")

def view_specific_patient():
    if len(patients) == 0:
        print("No patients to show")

    while True and len(patients) > 0:
        try:
            patient = int(input("Patient id:"))
            if patient not in patients:
                print("No patient record found for ", patient)
            else:
                print(patients[patient])
                break
        except:
            print("Patient id must be an int")

def remove_patient():
    while True and len(patients) > 0:
        try:
            patient = int(input("Patient id:"))
            if patient not in patients:
                print("No patient record found for ", patient)
            else:
                #del patients[patient]
                patients.pop(patient)
                print("Patient was successfully removed")
                break
        except:
            print("Patient id must be an int")
def main():
    while True:
        print("Menu\n========")
        print("1. Add a new patient")
        print("2. Remove a record")
        print("3. List all pets")
        print("4. List a specific pet based on patient number")
        print("5. List all data (patient #, type, name, age) for all pets")
        print("6. Exit")

        choice = input("Choice:")
        if choice == "1":
            add_pet()
        elif choice == "2":
            remove_patient()
        elif choice == "3":
            view_all_pets()
        elif choice == "4":
            view_specific_patient()
        elif choice=="5":
            view_all_data()
        elif choice == "6":
            print("Thank you for using this system")
            exit(0) #you can also use break
        else:
            print("Invalid choice. Pick a choice between 1-6")

main()