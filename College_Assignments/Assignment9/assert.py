try:
    mystring = "Hello"
    assert mystring == "Hi", "You should use 'Hi'"

except AssertionError as obj:
    print(obj)
