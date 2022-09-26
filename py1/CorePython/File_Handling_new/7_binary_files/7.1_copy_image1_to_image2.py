# copy an image into a file:
# open the file in binary mode : using the letter b

f1 = open("old_photo.jpeg", "rb")
f2 = open("new_photo.jpeg", "wb")

bytes = f1.read()
f2.write(bytes)

f1.close()
f2.close()
