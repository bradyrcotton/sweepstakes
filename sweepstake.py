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
        self.contestants[reg_number] = contestant




    def pick_winner(self):
        winner = user_interface.get_random_number(0, len(self.contestants))
        print(winner)
        return winner
    # print_contestant_info(self, contestant)
Sweepstake().register_contestant()
Sweepstake().register_contestant()
Sweepstake().register_contestant()
Sweepstake().register_contestant()
Sweepstake().pick_winner()