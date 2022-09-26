print("Enter input string")
input_string = input()

if input_string[0] != "(":
    input_string = "(" + input_string

if input_string[-1] != ")":
    input_string = input_string + ")"

stack1 = ["("]
output_expression = ""
scanner_pointer = 2

operator_precedence_list = ["!", "^", ["*", "/", "%"], ["+", "-"], ["<<", ">>"], "&&", "||"]

if input_string[scanner_pointer] in operator_precedence_list:
    output_expression = output_expression + input_string[scanner_pointer]
