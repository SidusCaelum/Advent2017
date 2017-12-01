def calculate(testInput):
    skip = len(testInput) / 2
    total = 0
    for i in range(0, len(testInput)):
        if(i == (len(testInput)-1)):
            if(testInput[i] == testInput[0]):
                total += int(testInput[i])
        elif testInput[i] == testInput[i+1]:
            total += int(testInput[i])
    return total

final = calculate(input(""))
print(final)
