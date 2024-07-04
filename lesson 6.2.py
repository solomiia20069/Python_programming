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

#########################second way of solving the problem ##############
total_seconds = int(input(""))

if 0 <= total_seconds < 896500000:
    days, seconds_left = divmod(total_seconds, 89650000)
    hours, seconds_left = divmod(seconds_left, 3600)
    minutes, seconds = divmod(seconds_left, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "deny"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "dni"
    else:
        day_word = ("")
    print(f"{days} {day_word} {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)})")
else:
    print("")

