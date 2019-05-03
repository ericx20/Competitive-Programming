alphabet = "abcdefghijklmnopqrstuvwxyz"
string = sorted(input())
anagram = sorted(input())
isAnagram = True
for letter in alphabet:
	if anagram.count(letter) > string.count(letter):
		isAnagram = False
		break
if isAnagram:
	print("A")
else:
	print("N")
