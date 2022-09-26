from ctypes import *

so_file = "/home/aditya/prj_ws/c_prjs/myfunctions.c"
my_functions = CDLL(so_file)
