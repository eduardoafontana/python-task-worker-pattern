
from domain import DomainClass
from task import DomainTask

class DomainService:

    @staticmethod
    def get_task_worker(quantity = None):

        domain_obj = DomainClass()
        domain_obj.set_quantity(quantity)

        task = DomainTask(domain_obj)

        return task
