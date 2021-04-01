import user_interface
from contestant import Contestant


class Sweepstake:

    def __init__(self):
        self.contestants = {

        }

    def register_contestant(self):
        first_name = user_interface.get_string_input('Please enter your first name!')
        last_name = user_interface.get_string_input('Please enter your last name!')
        email = user_interface.get_string_input('Please enter your email!')
        unique_key = len(self.contestants)
        reg_number = unique_key
        contestant = Contestant(first_name, last_name, email, reg_number)
        self.contestants[unique_key] = contestant



    # pick_winner()
    #
    # print_contestant_info(self, contestant)
Sweepstake().register_contestant()
print(Sweepstake().contestants[0])