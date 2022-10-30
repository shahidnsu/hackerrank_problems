path = "UDDDUDUU"
steps = 8


def countingValleys(steps, path):
    valleyCount = 0
    count = 0
    for i in path:
        if i == "U":
            count += 1

            if count == 0:
                valleyCount += 1
        else:
            count -= 1

    return valleyCount


print(countingValleys(steps, path))
