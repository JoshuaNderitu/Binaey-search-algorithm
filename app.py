# a function that takes alist and a target parameter
# multiple variables: middle, start, end, steps
#recursion or while loop
#increase steps each time a split is done
#condition to track target position


def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print(f'Step {steps} : {str(list[start:end+1])}')

        steps = steps +1
        middle = (start + end)// 2

        if element == list[middle]:
            return middle
        elif element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    
    return -1

my_list = [1,2,3,4,5,6,7,8,9 ]
target = 2

binary_search(my_list, target)
