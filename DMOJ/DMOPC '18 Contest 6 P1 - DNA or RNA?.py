input()
myinput = input()
other = False
DNA = False
RNA = False
for char in myinput:
    if char not in "ACGTU":
        other = True
        break
    else:
        if char == "T":
            DNA = True
        elif char == "U":
            RNA = True
if other:
    print("neither")
else:
    if (not DNA) and (not RNA):
        print("both")
    elif DNA and RNA:
        print("neither")
    elif DNA:
        print("DNA")
    else:
        print("RNA")
