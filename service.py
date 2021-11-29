
from domain import DomainClass
from task import DomainTask

class DomainService:

    @staticmethod
    def get_task_worker():

        domain_obj = DomainClass()
        domain_obj.set_quantity(30)

        task = DomainTask(domain_obj)

        return task
