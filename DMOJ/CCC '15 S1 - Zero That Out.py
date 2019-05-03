k = int(input())
sequence = []
for i in range(k):
    statement = int(input())
    if statement == 0:
        sequence.pop()
    else:
        sequence.append(statement)
print(sum(sequence))
