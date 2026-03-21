def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)
    
countdown(100)