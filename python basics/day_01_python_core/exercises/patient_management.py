patients = {}

blood_groups = {"A+","A-","B+","B-","AB+","AB-","O+","O-"}

def add_patient(name, age, blood_group, diseases,contact_numbers, emergency_contact_information):
    if blood_group not in blood_groups:
        print("Blood group is not valid. Please enter a valid blood group")
        return
    if len(patients)==0:
        patients["id"] = 1
        patients[1] = {}
        patients[1]["name"] = name
        patients[1]["age"] = age
        patients[1]["blood_group"] = blood_group
        patients[1]["diseases"] = diseases
        patients[1]["contact_numbers"] = contact_numbers
        patients[1]["emergency_contact_information"] = emergency_contact_information
    else:
        patients["id"] = list(patients.keys())[-1] + 1
        patients[patients["id"]] = {}
        patients[patients["id"]]["name"] = name
        patients[patients["id"]]["age"] = age
        patients[patients["id"]]["blood_group"] = blood_group
        patients[patients["id"]]["diseases"] = diseases
        patients[patients["id"]]["contact_numbers"] = contact_numbers
        patients[patients["id"]]["emergency_contact_information"] = emergency_contact_information

def search_patient_by_id(id):
    if id in patients:
        return patients[id]

def update_patient(id, name=None, age=None, blood_group=None, diseases=None, contact_numbers=None, emergency_contact_information=None):
    if id in patients:
        if name is not None:
            patients[id]["name"] = name
        if age is not None:
            patients[id]["age"] = age
        if blood_group is not None:
            if blood_group in blood_groups:
                patients[id]["blood_group"] = blood_group
            else:
                print("Blood group is not valid. Please enter a valid blood group")
        if diseases is not None:
            patients[id]["diseases"] = diseases
        if contact_numbers is not None:
            patients[id]["contact_numbers"] = contact_numbers
        if emergency_contact_information is not None:
            patients[id]["emergency_contact_information"] = emergency_contact_information

def add_disease_to_patient(id, disease):
    if id in patients:
        patients[id]["diseases"].append(disease)
        print("Disease added successfully.")

def remove_disease_from_patient(id, disease):
    if id in patients:
        if disease in patients[id]["diseases"]:
            patients[id]["diseases"].remove(disease)
            print("Disease removed successfully.")
        else:
            print("Disease not found for the patient.")

def all_diseases_recorded_in_hospital():
    diseases_recorded = []
    for id in patients:
        diseases_recorded.append(patients[id]["diseases"])

    diseases_set = set(diseases_recorded)
    return diseases_set

def get_patient_having_disease(disease):
    for id in patients:
        if disease in patients[id]["diseases"]:
            return patients[id]

def get_patient_having_blood_group(blood_group):
    if blood_group not in blood_groups:
        print("Blood group is not valid. Please enter a valid blood group")
        return
    for id in patients:
        if patients[id]["blood_group"] == blood_group:
            return patients[id]

def get_patients():
    return patients

def remove_patient(id):
    if id in patients:
        del patients[id]
        print("Patient removed successfully.")
    else:
        print("Patient not found.")

def get_patient_with_most_diseases():
    max_diseases = 0
    patient_with_most_diseases = None
    for id in patients:
        if len(patients[id]["diseases"]) > max_diseases:
            max_diseases = len(patients[id]["diseases"])
            patient_with_most_diseases = patients[id]
    return patient_with_most_diseases


