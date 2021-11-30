
from service import DomainService
import time

def start_method(message):
    print('Started in app. Message: ' + message)

def cancel_method(message):
    print('Cancelled in app. Message: ' + message)

def progress_method(message):
    print('Pregress in app. Message: ' + message)

def finished_method(data):
    print('Finished in app. Data: ' + data.data)

def datachange_method(data):
    print('Data changed in app. Data: ' + data.data)

# calling forever until cancel

task = DomainService.get_task_worker()
task.assign_start_callback(start_method)
task.assign_cancel_callback(cancel_method)
task.assign_progress_callback(progress_method)
task.assign_finished_callback(finished_method)
task.assign_datachange_callback(datachange_method)

task.start()

print('started main waiting')
time.sleep(3)
print('finished main waiting')

task.cancel()