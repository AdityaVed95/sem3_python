class Emp:
    def __init__(self, name, salary, ):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)
        print(self.salary)


e1 = Emp("Aditya", 3000)
print(hasattr(e1, 'name'))
print(getattr(e1, 'name'))
setattr(e1, 'name', 'Name1')

e1.show()
