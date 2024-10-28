#1) შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.
def add_five(number):
    return number + 5

#2)  შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს

def multiply(a, b):
    return a * b

#3) შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len()).

def string_length(s):
    return len(s)

#4)შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).

def list_of_lengths(strings):
    return [len(s) for s in strings]

#5)შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. ფუნქციამ უნდა იპოვოს ამ ლისტში შემავალი რიცხვების ჯამი

numbers = [1, 2, 3, 4, 5]
result = sum_of_list(numbers)
print(result)

#6) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგები და ინტეჯერები რაღაც თანმიმდევრობით. ფუნქციამ უნდა შეძლოს და ეს სტრინგების და ინტეჯერების თანმიმდევრობა უნდა გამოიტანოს შებრუნებულად.

def reverse_elements(*args):
    return list(args)[::-1]

#7) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგების ლისტი. ამ ფუნქციამ უნდა იპოვოს ყველაზე გრძელი და ყველაზე მოკლე სტრინგები ამ ლისტში.

def find_longest_and_shortest(strings):
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    return longest, shortest

#8) შექმენით ფუნქცია რომელსაც გადაეცემა რაიმე სტრინგი. ამ ფუნქციამ უნდა შეძლოს და თითოეული ასო შეცვალოს (პატარა ასო დიდი ასოთ a-A ხოლო დიდი ასო პატარათი A-a).

def swap_case(s):
    return s.swapcase()

#9) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი. ამ ფუნქციის მეშვეობით უნდა დაითვალოთ თანხმოვნების რაოდენობა ამ სტრინგში.

def count_consonants(s):
    consonants = "hello world"
    count = sum(1 for char in s if char in consonants)
    return count

#10) შექმენით ფუნქცია რომელსაც გადაეცემა ინტეჯერი და თუ ლუწია აბრუნებს True-ს ხოლო თუ კი კენტია აბრუნებს False

def is_even(number):
    return number % 2 == 0

#11) შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. თქვენი დავალებაა, რომ ამ სიის ლუწ ინდექსებზე მყოფი რიცხვების ჯამი დააბრუნოთ. აუცილებლად გამოიყენეთ return ამ და ასევე შემდეგ დავალებებში.

def sum_even_index(numbers):
    return sum(numbers[i] for i in range(0, len(numbers), 2))

#12)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ ლუწია თუ კენტი ის.

def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

#13)შექმენით ფუნქცია, რომელიც დააბრუნებს მარტივია თუ არა რიცხვი (მარტივია რიცხვი, თუ მას მარტო ორი გამყოფი აქვს).

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#14)შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. თქვენი დავალებაა, რომ დააბრუნოთ ამ სიის განახლებული ვერსია, სადაც ყველა სახელი დიდი ასოთი დაიწყება.

names_list = ["alice", "bob", "charlie"]
updated_names = capitalize_names(names_list)
print(updated_names)

#15)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. შემდეგ გამოიყენეთ ციკლი, რათა განიხილოთ ამ სიის ყველა რიცხვი - თუ რიცხვი ლუწია, ახალ სიაში დაამატეთ მისი განაყოფი ორზე, ხოლო თუ კენტია, მაშინ რიცხვის ნამრავლი ორზე. საბოლოოდ დააბრუნეთ განახლებული სია/ 

def process_numbers(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:  
            new_list.append(number // 2)  
        else:  
            new_list.append(number * 2) 
    return new_list

#16)შექმენით ფუნქცია, რომელსაც გადაეცემა სტრინგი და დააბრუნეთ ეს სტრინგდი შებრუნებულ + დიდი ასოებით (reversed / upper). 

def reverse_uppercase(input_string):
    return input_string[::-1].upper()

#17)შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან ---> (["dato" , "nika" , "polieqtori" , "zaza"....)], დამატებით შექმენით ორი სია odd = [] და even = [], გადაუარეთ ორიგინალ სიას for ციკლით და გაიგეთ რომელი ელემენტი შედგება კენტი ასოებისგან და რომელი ლუწი, საბოლოოდ ჩაამატეთ შესაბამისი სტრინგები შესაბამის სიებში (odd / even) დიდ ასოებათ (upper) და ბოლოს დაბეჭდეთ. 

def separate_strings_by_length(strings):
    odd = []   
    even = [] 
    
    for string in strings:
        if len(string) % 2 == 0:  
            even.append(string.upper())  
        else: 
            odd.append(string.upper())    
    
    print("Odd length strings:", odd)
    print("Even length strings:", even)


strings_list = ["dato", "nika", "polieqtori", "zaza", "hello", "world"]
separate_strings_by_length(strings_list)

#18) შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან, გადაუარეთ ამ სიას და შეამოწმეთ თუ მისი characterების რაოდენობა არის ლუწი, ჩაამატეთ ეს კონკრეტული სიის ელემენტი ახალ ცარიელ სიაში და გადააკეთეთ იგი upper ფუნქციით, თუ იქნება ამ სტრინგის ასოების რაოდენობა კენტი, ჩაამატეთ ეს ელემენტი ახალ სიაში რომელსაც პირველი character ექნება გადიდებული, დანარჩენი პატარა. საბოლოოდ გამოიტანეთ ეს სია. 

def process_strings(strings):
    new_list = []  
    
    for string in strings:
        if len(string) % 2 == 0:  
            new_list.append(string.upper())  
        else: 
            new_list.append(string.capitalize())  

    return new_list

