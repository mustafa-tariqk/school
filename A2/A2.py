import fun_math

def main():
    task = int(input("Please choose your task:\n"\
                     "1 – calculate factorial\n"\
                     "2 - generate a list of multiples\n"\
                     "3 – find max number in a list\n"))
    
    if task == 1:
        base = int(input("Please enter a positive integer: "))
        print(fun_math.cal_factorial(base))

    elif task == 2:
        number, length = input("Please enter a non-negative number and a length: ").split()
        print(fun_math.list_multiples(int(number), int(length)))

    elif task == 3:
        a_list = input("Please enter a list of integers: ")
        print(fun_math.find_max(a_list.split()))
        
main()