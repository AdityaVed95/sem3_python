operator_precedence_list = ["!", "^", ["*", "/", "%"], ["+", "-"], ["<<", ">>"], "&&", "||"]
input_string = "*hello world"

if input_string[0] in operator_precedence_list:
    print("Is there")

# elif input_string[0] in

for item in operator_precedence_list:
    if type(item) == "<class 'list'>":
        print(item)
