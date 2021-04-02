from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakesQueueManager
import user_interface


class MarketingFirmCreator:

    def __init__(self):
        self.queue = SweepstakesQueueManager()
        self.stack = SweepstakesStackManager()

    def choose_manager(self):
        manager = user_interface.get_string_input('Please choose manager type: Press: [1] for Queue or Press: [2] for Stack.')
        if manager == 1:
            SweepstakesQueueManager()
        elif manager == 2:
            SweepstakesStackManager()
        else:
            return
