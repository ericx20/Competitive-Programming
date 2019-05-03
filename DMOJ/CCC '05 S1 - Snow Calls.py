charToNum = ["", "", "ABC", "DEF", "GHI", "JKL",
             "MNO", "PQRS", "TUV", "WXYZ"]
for i in range(int(input())):
    inputNum = input().replace("-", "")
    outputNum = ""
    for char in inputNum:
        try:
            int(char)  # throw it away, just wanted to check if it's a number
            outputNum += char
        except ValueError:
            for j in range(2, 10):
                if char in charToNum[j]:
                    outputNum += str(j)
                    break
    properOutput = ""
    for start, end in [[0, 2], [3, 5], [6 ,9]]:
        properOutput += outputNum[start:end+1]
        if start != 6:
            properOutput += "-"
    print(properOutput)
