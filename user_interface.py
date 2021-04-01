

def get_string_input(inputs):
    u_input = input(inputs)
    return u_input
    # return input from user as a string



def contestant_info():
    first_name = input("Enter First Name")
    last_name = input("Enter Last Name")
    email = input("Enter Email")
    contestant = (first_name, last_name, email, reg_number)
    return contestant


# def update_dict():
#     contestants = contestant_info()
#     Sweepstake().contestants.update(contestants)


# update_dict()