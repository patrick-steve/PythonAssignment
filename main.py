CHOSEN_ROLE = ""

def crud_user(op, data):
    match op:
        case "create":
            with open("users.json", 'w') as f:
                f.write()
    

def run():
    exit = False
    while not exit:
        print("Welcome to South Side Hospital Management System : ")
        print("Please select your role : ")
        print("\t1.Administrator\n\t2.Doctor\n\t3.Nurse\n\t4.Receptionist\n\t5.Patient")
        ri = input("")
        match ri:
            case "1":
                print("You have choosen the Administrator role ! ")
                ROLE = "Administrator"
            case "2":
                print("You have choosen the Doctor role ! ")
                ROLE = "Doctor"
            case "3":
                print("You have choosen the Nurse role ! ")
                ROLE = "Nurse"
            case "4":
                print("You have choosen the Receptionist role ! ")
                ROLE = "Receptionist"
            case "5":
                print("You have choosen the Patient role ! ")
                ROLE = "Patient"
            case _:
                print("Invalid role !")

