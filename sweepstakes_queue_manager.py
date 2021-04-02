from sweep_queue import Queue
import user_interface


class SweepstakesQueueManager:

    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self):
        sweepstake = user_interface.get_string_input('Please input sweepstake')
        self.queue.enqueue(sweepstake)

    def get_sweepstake(self):
        self.queue.dequeue()