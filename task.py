
import threading
import time

class TaskData:
    def __init__(self, value):
        self.data = value

class DomainTask:

    def __init__(self, domain_object):
        self.domain_object = domain_object
        self.executing = False
        self.cancelled = False
        self.start_callback = None
        self.cancel_callback = None
        self.progress_callback = None
        self.finished_callback = None
        self.datachange_callback = None

    def start(self):
        self.executing = True
        if self.start_callback: self.start_callback('Execution started.')

        thread = threading.Thread(name="domain_task", target = self._execute, args = ())
        thread.start()

    def _execute(self):
        count = 0
        while self.executing and ((self.domain_object.quantity and count < self.domain_object.quantity) or not self.domain_object.quantity):
            count = count + 1
            if self.progress_callback: self.progress_callback('Executing... count: ' + str(count))

            if count % 10 == 0:
                if self.datachange_callback: 
                    task_data = TaskData('data changed value: ' + str(count))
                    self.datachange_callback(task_data)

            time.sleep(0.2)

        if not self.cancelled:
            task_data = TaskData('data fisnished value')
            if self.finished_callback: self.finished_callback(task_data)

    def cancel(self):
        self.executing = False
        self.cancelled = True
        if self.cancel_callback: self.cancel_callback('Execution cancelled.')
    
    def assign_progress_callback(self, callback_method):
        self.progress_callback = callback_method

    def assign_cancel_callback(self, callback_method):
        self.cancel_callback = callback_method

    def assign_start_callback(self, callback_method):
        self.start_callback = callback_method

    def assign_finished_callback(self, callback_method):
        self.finished_callback = callback_method

    def assign_datachange_callback(self, callback_method):
        self.datachange_callback = callback_method