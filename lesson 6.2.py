time = float(input("Enter number from 0 to 8640000 "))

if 0 <= time <= 8640000:
    day = time // (24 * 3600)
    time = time % (24 * 3600)

    hour = time // 3600
    time = time % 3600

    minute = time // 60
    time = time % 60

    second = time
    if day == 0:
        print("%d day, %d:%d:%d" % (day, hour, minute, second))
    else:
        print("%d days, %d:%d:%d" % (day, hour, minute, second))

else:
    print("Error! Enter the number between 0 and 8640000")
