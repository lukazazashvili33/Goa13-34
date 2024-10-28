# 1) დაბეჭდეთ რიცხვები 1-დან 5-მდე for loop-ის გამოყენებით.
def print_numbers_for():
    for i in range(1, 6):
        print(i)

# 2) ამობეჭდეთ რიცხვები 1-დან 5-მდე while loop-ის გამოყენებით.
def print_numbers_while():
    i = 1
    while i <= 5:
        print(i)
        i += 1

# 3) ამობეჭდეთ თითოეული სიმბოლო სტრიქონში "hello" for loop-ის გამოყენებით.
def print_characters_for():
    for char in "hello":
        print(char)

# 4) ამობეჭდეთ თითოეული სიმბოლო სტრიქონში "hello" while loop-ის გამოყენებით.
def print_characters_while():
    i = 0
    while i < len("hello"):
        print("hello"[i])
        i += 1

# 5) დაბეჭდეთ რიცხვები 1, 2, 3 for loop-ის გამოყენებით.
def print_specific_numbers_for():
    for i in [1, 2, 3]:
        print(i)

# 6) ამობეჭდეთ რიცხვები 1, 2, 3 while loop-ის გამოყენებით.
def print_specific_numbers_while():
    numbers = [1, 2, 3]
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

# 7) დაბეჭდეთ „პითონი სახალისოა“ 3-ჯერ for loop-ის გამოყენებით.
def print_message_for():
    for _ in range(3):
        print("პითონი სახალისოა")

# 8) ამობეჭდეთ „პითონი სახალისოა“ 3-ჯერ while loop-ის გამოყენებით.
def print_message_while():
    count = 0
    while count < 3:
        print("პითონი სახალისოა")
        count += 1

# 9) დაბეჭდეთ სიის ელემენტები [1, 2, 3] for loop-ის გამოყენებით.
def print_list_for():
    for item in [1, 2, 3]:
        print(item)

# 10) ამობეჭდეთ სიის ელემენტები [1, 2, 3] while loop-ის გამოყენებით.
def print_list_while():
    items = [1, 2, 3]
    i = 0
    while i < len(items):
        print(items[i])
        i += 1

# 11) დაბეჭდეთ "hi" თითოეული ელემენტისთვის სიაში [1, 2, 3] for loop-ის გამოყენებით.
def print_hi_for():
    for _ in [1, 2, 3]:
        print("hi")

# 12) ამობეჭდეთ "hi" თითოეული ელემენტისთვის სიაში [1, 2, 3] while loop-ის გამოყენებით.
def print_hi_while():
    items = [1, 2, 3]
    i = 0
    while i < len(items):
        print("hi")
        i += 1

# 13) დაბეჭდეთ პირველი 3 დადებითი მთელი რიცხვი for loop-ის გამოყენებით.
def print_positive_integers_for():
    for i in range(1, 4):
        print(i)

# 14) ამობეჭდეთ პირველი 3 დადებითი მთელი რიცხვი while loop-ის გამოყენებით.
def print_positive_integers_while():
    i = 1
    while i <= 3:
        print(i)
        i += 1

# 15) ამობეჭდეთ რიცხვები 1-დან 3-მდე საპირისპიროდ for loop-ის გამოყენებით.
def print_reverse_for():
    for i in range(3, 0, -1):
        print(i)

# 16) ამობეჭდეთ რიცხვები 1-დან 3-მდე საპირისპიროდ, while loop-ის გამოყენებით.
def print_reverse_while():
    i = 3
    while i > 0:
        print(i)
        i -= 1

# 17) დაბეჭდეთ ანბანის პირველი 4 ასო for loop-ის გამოყენებით.
def print_alphabet_for():
    for char in "abcd":
        print(char)

# 18) ამობეჭდეთ ანბანის პირველი 4 ასო while loop-ის გამოყენებით.
def print_alphabet_while():
    i = 0
    while i < 4:
        print("abcd"[i])
        i += 1

# 19) დაბეჭდეთ შეტყობინება "looping" 4-ჯერ for loop-ის გამოყენებით.
def print_looping_for():
    for _ in range(4):
        print("looping")

# 20) დაბეჭდეთ შეტყობინება „looping“ 4-ჯერ while loop-ის გამოყენებით.
def print_looping_while():
    count = 0
    while count < 4:
        print("looping")
        count += 1

# 21) ამობეჭდეთ ტუპლის ელემენტები (1, 2, 3) for loop-ის გამოყენებით.
def print_tuple_for():
    for item in (1, 2, 3):
        print(item)

# 22) ამობეჭდეთ tuple-ის ელემენტები (1, 2, 3) while loop-ის გამოყენებით.
def print_tuple_while():
    items = (1, 2, 3)
    i = 0
    while i < len(items):
        print(items[i])
        i += 1

# 23) დაბეჭდეთ რიცხვები 5, 4, 3, 2, 1 for loop-ის გამოყენებით.
def print_reverse_numbers_for():
    for i in range(5, 0, -1):
        print(i)

# 24) ამობეჭდეთ რიცხვები 5, 4, 3, 2, 1 while loop-ის გამოყენებით.
def print_reverse_numbers_while():
    i = 5
    while i > 0:
        print(i)
        i -= 1

# 25) ამობეჭდეთ სიის ელემენტები ["ვაშლი", "ბანანი", "ალუბალი"] for loop-ის გამოყენებით.
def print_fruits_for():
    for fruit in ["ვაშლი", "ბანანი", "ალუბალი"]:
        print(fruit)
    
    # 26. ამობეჭდეთ სიის ელემენტები ["ვაშლი", "ბანანი", "ალუბალი"] while loop-ის გამოყენებით.
def print_fruits_while():
    fruits = ["ვაშლი", "ბანანი", "ალუბალი"]
    i = 0
    while i < len(fruits):
        print(fruits[i])
        i += 1

# 27. დაბეჭდეთ პირველი 3 რიცხვი 0-დან დაწყებული for loop-ის გამოყენებით.
def print_first_three_for():
    for i in range(3):
        print(i)

# 28. დაბეჭდეთ პირველი 3 ნომერი 0-დან დაწყებული while მარყუჟის გამოყენებით.
def print_first_three_while():
    i = 0
    while i < 3:
        print(i)
        i += 1

# 29. დაბეჭდეთ სიტყვა "loop" თითოეული რიცხვისთვის სიაში [1, 2, 3, 4] for loop-ის გამოყენებით.
def print_loop_for():
    for _ in [1, 2, 3, 4]:
        print("loop")

# 30. ამობეჭდეთ სიტყვა „მარყუჟი“ თითოეული რიცხვისთვის სიაში [1, 2, 3, 4] while loop-ის გამოყენებით.
def print_loop_while():
    numbers = [1, 2, 3, 4]
    i = 0
    while i < len(numbers):
        print("მარყუჟი")
        i += 1

# 31. დაბეჭდეთ "abc" სტრიქონის სიმბოლოები for loop-ის გამოყენებით.
def print_abc_for():
    for char in "abc":
        print(char)

# 32. ამობეჭდეთ სტრიქონის სიმბოლოები „abc“ while loop-ის გამოყენებით.
def print_abc_while():
    i = 0
    while i < len("abc"):
        print("abc"[i])
        i += 1

# 33. დაბეჭდეთ სიის პირველი 2 ელემენტი ["x", "y", "z"] for loop-ის გამოყენებით.
def print_first_two_for():
    for item in ["x", "y", "z"][:2]:
        print(item)

# 34. ამობეჭდეთ სიის პირველი 2 ელემენტი ["x", "y", "z"] while მარყუჟის გამოყენებით.
def print_first_two_while():
    items = ["x", "y", "z"]
    i = 0
    while i < 2:
        print(items[i])
        i += 1

# 35. დაბეჭდეთ შეტყობინება "Hello World" 2-ჯერ for loop-ის გამოყენებით.
def print_hello_world_for():
    for _ in range(2):
        print("Hello World")

# 36. ამობეჭდეთ შეტყობინება "Hello World" 2-ჯერ while loop-ის გამოყენებით.
def print_hello_world_while():
    count = 0
    while count < 2:
        print("Hello World")
        count += 1

# 37. ამობეჭდეთ სიმრავლის ელემენტები {1, 2, 3} for loop-ის გამოყენებით.
def print_set_for():
    for item in {1, 2, 3}:
        print(item)

# 38. ამობეჭდოთ ნაკრების ელემენტები {1, 2, 3} while მარყუჟის გამოყენებით.
def print_set_while():
    items = {1, 2, 3}
    i = iter(items)
    while True:
        try:
            print(next(i))
        except StopIteration:
            break

# 39. ლექსიკონის ელემენტების ამობეჭდვა {"a": 1, "b": 2} for loop-ის გამოყენებით.
def print_dict_for():
    for key, value in {"a": 1, "b": 2}.items():
        print(f"{key}: {value}")

# 40. ლექსიკონის ელემენტების ამობეჭდვა {"a": 1, "b": 2} while loop-ის გამოყენებით.
def print_dict_while():
    items = {"a": 1, "b": 2}
    keys = list(items.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        print(f"{key}: {items[key]}")
        i += 1

# 41. დაბეჭდეთ რიცხვები 10, 20, 30 for loop-ის გამოყენებით.
def print_specific_numbers_for():
    for num in [10, 20, 30]:
        print(num)

# 42. ამობეჭდეთ რიცხვები 10, 20, 30 while loop-ის გამოყენებით.
def print_specific_numbers_while():
    numbers = [10, 20, 30]
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

# 43. დაბეჭდეთ "შესრულებულია" for loop-ის დასრულების შემდეგ.
def print_completed_for():
    for _ in range(1):
        pass
    print("შესრულებულია")

# 44. დაბეჭდეთ "შესრულებულია" ცოტა ხნის მარყუჟის დასრულების შემდეგ.
def print_completed_while():
    count = 0
    while count < 1:
        count += 1
    print("შესრულებულია")

# 45. დაბეჭდეთ წყობილი სიის ელემენტები [[1, 2], [3, 4]] for loop-ის გამოყენებით.
def print_nested_list_for():
    for sublist in [[1, 2], [3, 4]]:
        for item in sublist:
            print(item)

# 46. ​​დაბეჭდეთ წყობილი სიის ელემენტები [[1, 2], [3, 4]] while მარყუჟის გამოყენებით.
def print_nested_list_while():
    nested_list = [[1, 2], [3, 4]]
    i = 0
    while i < len(nested_list):
        j = 0
        while j < len(nested_list[i]):
            print(nested_list[i][j])
            j += 1
        i += 1

# 47. დაბეჭდეთ პირველი 5 დადებითი მთელი რიცხვი for loop-ის გამოყენებით.
def print_first_five_positive_for():
    for i in range(1, 6):
        print(i)

# 48. ამობეჭდეთ პირველი 5 დადებითი მთელი რიცხვი while მარყუჟის გამოყენებით.
def print_first_five_positive_while():
    i = 1
    while i <= 5:
        print(i)
        i += 1

# 49. დაბეჭდეთ სტრიქონის "loop" თითოეული სიმბოლო for loop-ის გამოყენებით.
def print_loop_characters_for():
    for char in "loop":
        print(char)

# 50. დაბეჭდეთ სტრიქონის "loop" თითოეული სიმბოლო while loop-ის გამოყენებით.
def print_loop_characters_while():
    i = 0
    while i < len("loop"):
        print("loop"[i])
        i += 1

