def countDownAndUp(number):
    print(number)
    if number == 0:
        print("Reached base case.")
        return
    else:
        countDownAndUp(number-1)
        print(number, 'returning')
        return

countDownAndUp(5)

