# dynamic typing : passing int , float , strings and lists to the add fxn
def add(a, b):
    sum_up = a + b
    print(sum_up)
    print()
    return None


add(5, 7)
add(5.9, 3.1)
add([1, 2, 3, 4], [5, 6, 7])
add("Aditya", "Ved")
add("hello", str(34))
# no addition for dictionaries : add({"a": 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5})
