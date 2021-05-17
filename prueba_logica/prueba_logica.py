
def canBeSplitted(array_number):
    if len(array_number) <= 1:
        return 0
    n = len(array_number)       
    for i in range(n):
        left_part = sum(array_number[0:i]) 
        right_part = sum(array_number[i:n])
        if left_part == right_part:
            return 1
    return -1  

if __name__ == '__main__':
    array = [1,3,3,8,4,3,2,3,3]
    #array = [0,1,2,3,4,5,6,7,8,9]
    can = canBeSplitted(array)
    print(can)