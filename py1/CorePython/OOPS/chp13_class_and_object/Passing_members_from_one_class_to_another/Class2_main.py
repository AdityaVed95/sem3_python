class Class2:
    @staticmethod
    def mymethod(e):  # acts neither on class variable or instance varaible of Class2
        e.salary += 1000
        e.display()

    def hello(self):
        print("hello")
