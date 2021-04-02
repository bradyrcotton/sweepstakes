from stack import Stack
import user_interface


class SweepstakesStackManager:

    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self):
        sweepstake = user_interface.get_string_input('Please input sweepstake')
        self.stack.push(sweepstake)

    def get_sweepstake(self):
        self.stack.pop()
