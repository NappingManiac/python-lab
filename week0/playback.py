#Replace the spaces between a submitted string with three elipses.
#.replace("", "") should achieve what we want here.

userString = input("")
userString = userString.replace(" ", "...")
print(userString)