
from customer import Customer

class CustomerImplement(Customer):

    __name=""
    __phn=""
    __email=""
    __pad=""

    def __init__(self,name,phn,email,pad):

        self.__name=name
        self.__phn=phn
        self.__email=email
        self.__pad=pad

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_phn(self):
        return self.__phn

    def set_phn(self,phn):
        self.__phn=phn

    def get_email(self):
        return self.__email

    def set_email(self,email):
        self.__email=email

    def get_pad(self):
        return self.__pad

    def set_pad(self,pad):
        self.__pad=pad

    def __str__(self):
        return self.__name+" "+self.__phn+" "+self.__email+" "+self.__pad
