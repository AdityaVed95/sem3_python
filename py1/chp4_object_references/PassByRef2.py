f = [14, 23, 37]
print("initially f is : ", f)


def replace_individual_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g inside function is : ", g)


replace_individual_contents(f)

print("after replace_individual_contents , f is : ", f)
