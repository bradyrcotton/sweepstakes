


class Contestant:
    # first_name, last_name, email, registration_number
    def __init__(self, first_name, last_name, email, reg_number):
        self.contestant = {first_name: "", last_name: "", email: "", reg_number: ""}
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.reg_number = reg_number

    def __getitem__(self, key):
        return getattr(self, key)

