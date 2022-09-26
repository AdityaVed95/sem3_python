class Items:
    list1 = []
    list2 = []
    name1 = ""
    name2 = ""


object1 = Items()
object1.list2 = [324, 52, 352, 52, 523, 53]

object2 = Items()
object2.list2 = [432, 36, 623, 6, 43, 32]

final_list = object2.list2 + object1.list2
print(final_list)
