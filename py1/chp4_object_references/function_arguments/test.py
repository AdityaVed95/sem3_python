# check the warning of this program given by pycharm

def add_spam(menu=[]):
    menu.append("spam")
    return menu


breakfast = ["bacon", "eggs"]
print(breakfast)

add_spam(breakfast)
print(breakfast)

add_spam(breakfast)
print(breakfast)

add_spam(breakfast)
print(breakfast)

print(add_spam())
print(add_spam())
print(add_spam())
print(add_spam())
