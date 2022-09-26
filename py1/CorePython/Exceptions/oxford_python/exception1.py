class MyException(Exception):
    pass


def fxn1():
    print("Here the functioning of other program continues after the occurrence of exception :")


def main():
    try:
        raise MyException('Hello', 'World')

    except MyException as errorObj:
        print(errorObj)
        print(errorObj.args)
        print(type(errorObj))
        fxn1()


if __name__ == "__main__":
    main()
