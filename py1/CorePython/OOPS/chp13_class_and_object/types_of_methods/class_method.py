class Bird:
    # class variable
    wings = 2

    @classmethod
    def fly(cls, name):
        print("{} flies with {} wings ".format(name, cls.wings))


# classname.classmethodname()
# no need of creating an instance of the class in this case

Bird.fly("Sparrow")
Bird.fly("Pigeon")
