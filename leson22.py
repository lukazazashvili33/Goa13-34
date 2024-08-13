def filter_list(number_list):
    for num in number_list:
        if num % 2 == 0:
            print("even:", num)
        else:
            print("odd:", num)
            
filter_list([1,2,3,4,5,6,7,8,9,10])