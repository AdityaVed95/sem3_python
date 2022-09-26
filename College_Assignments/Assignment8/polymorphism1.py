class India:
    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi and English")


class USA:
    def capital(self):
        print("Washington DC")

    def language(self):
        print("English")


obj_ind = India()
obj_usa = USA()

for i in (obj_ind, obj_usa):
    print(i.capital())
    print(i.language())

print("==================")

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
