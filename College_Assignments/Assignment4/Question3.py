### dsa
# this is equivalent to comments: '''gfcffgjhhfry'''
import re

Txt = """Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
560-555-5153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com

Corey Jefferson
900-555-9340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.com"""

result1 = re.findall(r'\d{3}[-]\d{3}[-]\d{4}', Txt)

print("All the occurrences of Phone numbers are listed below:")
print(result1)
