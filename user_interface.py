from contestant import Contestant




def contestant_info ():
    first_name = input("Enter First Name")
    last_name = input("Enter Last Name")
    email = input("Enter Email")
    reg_number = input("Enter Registration Number")
    contestant = Contestant(first_name, last_name, email, reg_number)
    # print(contestant["first_name"])
    return contestant

