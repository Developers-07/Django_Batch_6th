# abstraction, encapsulation, inheritance, polymorphism

# abstraction --> system designing or system planning
from abc import ABC, abstractmethod


class Student(ABC):

    # class --> no body part, only signature

    @abstractmethod
    def get_stu_name(self):
        pass

    @abstractmethod
    def set_stu_name(self, name):
        pass

    @abstractmethod
    def get_stu_dept(self):
        pass

    @abstractmethod
    def set_stu_dept(self,dept):
        pass