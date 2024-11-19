CHOSEN_ROLE = ""

def crud_user(op, data):
    if CHOSEN_ROLE == "Administrator":
        match op:
            case "create":
                with open("users.txt", 'a') as f:
                    f.write(data+"\n")
                    f.close()
            case "get all":
                with open("users.txt", 'r') as f:
                    users = f.read()
                    f.close()
                    return users
            case "get with id":
                with open("users.txt", 'r') as f:
                    users = f.read().split(" ")
                    f.close()
                    return [user for user in users if user.split(" ")[0] == data] 
            case "update":
                with open("users.txt", 'w+r') as f:
                    users = f.read().split(" ")
                    uid_to_update = [i for (user, i) in enumerate(users) if user.split(" ")[0] == data][0]
                    users[uid_to_update] = data
                    f.write(user for user in users if user.split(" ")[0])
                    f.close()
            case "delete":
                with open("users.txt", 'w+r') as f:
                    users = f.read().split(" ")
                    uid_to_update = [i for (user, i) in enumerate(users) if user.split(" ")[0] == data][0]
                    users.remove(users[uid_to_update])
                    f.write(user for user in users if user.split(" ")[0])
                    f.close()
            case _:
                pass

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

