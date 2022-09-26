try:
    print("Enter no btw 5 and 10")
    x = int(input())
    assert 5 < x < 10, "Your input is not correct"
    print("you have entered : ", x)


except AssertionError as obj1:
    print(obj1)
