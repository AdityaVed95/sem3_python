def add_spam(menu=None):
    if menu is None:
        menu = []
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
