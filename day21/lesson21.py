#1)
def add_five(number):
    return number + 5
#მაგალით
print(add_five(10))  # Output: 15
print(add_five(0))   # Output: 5
print(add_five(-7))  # Output: -2

#2)
def multiply(a, b):
    return a * b
#'a*b' ფუნქცია იღებს ორ არგუმენტს ა და ბ არის ინტეჯერები და აბრუნებსორივეს ნამრავლს 
#ინტეჯერი არის მთელი რიცხვი, რომელიც არ შეიცავს ათწილადს ან дробს. ინტეჯერები შეიძლება იყვნენ როგორც დადებითები, ასევე უარყოფითები და ნული.

#3)
def string_length(s):
    return len(s)
#len(s): ეს ფუნქცია ითვლის სტრიქონში სიმბოლოების რაოდენობას და აბრუნებს შედეგს. თუ სტრიქონი ცარიელია მაშინ შედეგს გამოიტანს ნულს.

#4)
def list_of_lengths(strings):
    return [len(s) for s in strings]
#[len(s) for s in strings]: ეს არის ლისტის კომპრეჰენშენი (list comprehension), რომელიც იტერირებს strings სიაში თითოეულ ელემენტზე და იყენებს len()-ს, რომ მიიღოს თითოეული სტრიქონის სიგრძე.

#5)
def is_palindrome(s):
      # ვაქცევთ სტრიქონს პატარა ასოებად და ვამოწმებთ, არის თუ არა იგივე ამობრუნებულ ვერსიასთან
    return s == s[::-1]

#6) 
def longest_string(strings):
    if not strings:
        return None  # თუ სია ცარიელია, ვაბრუნებთ None-ს
    return max(strings, key=len)

#7)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    #რიცხვი n არის n-ის და მასზე ნაკლები ყველა დადებითი მთელი რიცხვის ნამრავლი. მაგალითად, 5! = 5 * 4 * 3 * 2 * 1 = 120.

#8)
def sum_of_maxima(list1, list2):
    max1 = max(list1)
    max2 = max(list2)
    return max1 + max2
#max(list1): ფუნქცია max() გამოიყენება პირველი სიიდან მაქსიმალური ელემენტის მისაღებად.

#9)
def difference_of_minima(list1, list2):
    if not list1 or not list2:
        raise ValueError("Both lists must be non-empty")
    
    min1 = min(list1)
    min2 = min(list2)
    
    return abs(min1 - min2)
#min(list1): min() ფუნქცია გამოიყენება პირველი სიიდან მინიმალური ელემენტის მისაღებად

#10)
def range_of_list(numbers):
    if not numbers:
        raise ValueError("The list must be non-empty")
    
    max_num = max(numbers)
    min_num = min(numbers)
    
    return max_num - min_num
#max(numbers): max() ფუნქცია ნახავს სიაში მაქსიმალურ ელემენტს 