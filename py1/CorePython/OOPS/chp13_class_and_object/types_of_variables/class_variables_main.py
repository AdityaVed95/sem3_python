class Sample:
    x = 10  # class variable

    @classmethod  # class method
    def modify(cls):
        cls.x += 1


s1 = Sample()
s2 = Sample()

print("x is s1 is : ", s1.x)
print("x in s2 is : ", s2.x)

s1.modify()

print("x is s1 is : ", s1.x)
print("x in s2 is : ", s2.x)
