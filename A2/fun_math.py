def cal_factorial(x):
    if x < 2:
        return 1
    else: 
        return x * cal_factorial(x-1)

def list_multiples(number, length):
    multiples = []
    for i in range(1,length+1):
        multiples.append(number * i)
    return multiples

def find_max(a_list):
    max = a_list[0]
    for a in a_list[0:]:
        if max < a:
            max = a
    return max


if __name__ == "__main__":
    print(cal_factorial(4))

    print(list_multiples(2,3))
    print(list_multiples(7,5))

    print(find_max([1,3,4,2,1,3,4,5,7,1,3,4,5,6,2,6,123,436,124,213]))
