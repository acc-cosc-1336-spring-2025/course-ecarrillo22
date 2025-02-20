def get_factorial(num):

    factorial = 1

    for num in range (1, num+1):
        
        factorial *= num
        
    return factorial

def sum_odd_numbers(num):
    
    sum = 0


    while(num > 0):
        
        if num % 2 != 0:
            sum += num
            
        num -= 1


    return sum