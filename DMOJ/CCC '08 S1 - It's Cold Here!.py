done = False
coldestSoFar = 201
coldestCity = ""
while not done:
	city, temp = input().split()
	temp = int(temp)
	if city == "Waterloo":
		done = True
	if temp < coldestSoFar:
		coldestSoFar = temp
		coldestCity = city
print(coldestCity)
