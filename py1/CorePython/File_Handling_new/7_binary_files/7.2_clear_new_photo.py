# the purpose of this program is to clear the new photo so that we can run
# 7.1 program again to check its functionality


f1 = open("new_photo.jpeg", "wb")
f1.write(b"")
f1.close()
