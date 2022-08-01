
from abc import ABC, abstractmethod

class Customer(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self,name):
        pass

    @abstractmethod
    def get_phn(self):
        pass

    @abstractmethod
    def set_phn(self,phn):
        pass

    @abstractmethod
    def get_email(self):
        pass

    @abstractmethod
    def set_email(self,email):
        pass

    @abstractmethod
    def get_pad(self):
        pass

    @abstractmethod
    def set_pad(self,pad):
        pass



