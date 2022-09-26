def avg_sum(iterable):
    try:
        sum = 0

        for item in iterable:
            sum += item

        average = sum / len(iterable)

        return average, sum

    except TypeError:
        print("please enter correct data types ")
        return None, None

    except ZeroDivisionError:
        print("please dont pass empty iterables")
        return None, None


def main():
    a, t = avg_sum(())
    print(a, t)


if __name__ == "__main__":
    main()
