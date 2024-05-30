
def attendance(n):
    maxMiss = 4
    attendanceLog = [1] * (maxMiss + 1)
    attendanceLog[maxMiss] = 0

    for i in range(1, n + 1):
        temp = [0] * (maxMiss + 1)
        for j in range(maxMiss - 1, -1, -1):
            temp[j] = attendanceLog[0] + attendanceLog[j + 1]

        temp, attendanceLog = attendanceLog, temp

    validClass = attendanceLog[0]
    lastDayMiss = temp[1]
    print(validClass)
    print(f"{lastDayMiss}/{validClass}")
    return f"for {n} days: {lastDayMiss}/{validClass}"


if __name__ == "__main__":
    print(attendance(5))  # Output: 14/29
    print(attendance(10)) # Output: 372/773
