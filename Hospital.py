import json
import colorama
import os

from colorama import Fore, Back, Style
from colorama import init

init()
print(Fore.RED)


def search_patient(name):
    with open("E:\\Dev\\Python\\1-27\\patients.json", "r") as f:
        patients = json.load(f)
        for patient in patients:
            if patient["name"] == name:
                return patient


new_patient = input("Do you want to add a new patient?(y/n) ")
if new_patient == "y":
    new_patient = "True"
    name = str(input("What is the name of the patient: "))
    age = int(input("What is the age of the patient: "))
    weight = int(input("What is the weight of the patient (lb): "))
    height = int(input("What is the height of the patient (cm): "))
    print("Done adding new patient")
    print("The patients data is:")
    print("Name:", name, "\nAge:", age,
          "\nWeight:", weight, "\nHeight:", height)
    with open("E:\\Dev\\Python\\1-27\\patients.json", "r") as f:
        patients = json.load(f)
    patients.append({"name": name, "age": age,
                    "weight": weight, "height": height})
    with open("E:\\Dev\\Python\\1-27\\patients.json", "w") as f:
        json.dump(patients, f)
else:
    new_patient = "False"
    name = input("What is the name of the patient: ")
    retrieve_patient = input("Do you want to retrieve the patient data?(y/n) ")
    if retrieve_patient == "y":
        patient_data = search_patient(name)
        if patient_data:
            print("The patient's data is: ", "\nName:", patient_data["name"], "\nAge:",
                  patient_data["age"], "\nWeight:", patient_data["weight"], "\nHeight:", patient_data["height"])
        else:
            print("No patient found with that name.")
    else:
        print("Ok.")
