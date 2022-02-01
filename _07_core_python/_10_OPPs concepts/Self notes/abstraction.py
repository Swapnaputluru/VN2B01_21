from abc import ABC, abstractmethod


class A(ABC):
    @ abstractmethod
    def addition(self):
        None


class B(A):
    def addition(self):
        print("addition")

obj = B()
obj.addition()