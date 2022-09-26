# print("input your age :")
# x = input()
# print("you entered :", x)
import sys

print("Hello to stdout :", file=sys.stdout)  # this printed line will go to standard output stream

print("Hello to stderr :", file=sys.stderr)  # this printed line will go to standard error stream

# when we run the program : the output of stdout and stderr both is printed on the screen
# inorder to print only output we can put the standard error to another file and similarly
# inorder to print only error we can put the standard output to another file
# we can also put both stdout and stderr to two diff files and then cat the file to see its contents
