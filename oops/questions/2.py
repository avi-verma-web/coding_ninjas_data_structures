class Student:
    name = 'Parikh'
    def __init__(self,name):
        self.name=name
    def store_details(self):
        self.age = 60
    def print_details(self):
        print(self.name,Student.name, end=' ')
        print(self.age)
s = Student("something")
s.store_details()
s.print_details()