def numerbs1to100(text1, text2)-> int:
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1, text2)
            continue
        elif i % 3 == 0: 
            print(text1)
            continue
        elif i % 5 == 0: 
            print (text2)
            continue
        else:
            print(i) 
            contador += 1
    
    return contador

print(numerbs1to100("Fizz", "Buzz"))
