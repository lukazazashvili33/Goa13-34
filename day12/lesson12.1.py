#მომხმარებელს შემოატანინეთ ტექსტში მიღებული ქულა თუ ქულა მეტია 90 - ზე და ნაკლებია 100 ზე მაგ შემთხვევაში დაპრინტეთ. თქვენ დაგიფინანსდებათ სწავლა სრულიად თუ მიღებული ქულა  მეტია 70 ზე და ნაკლებია 80 ზე მაგ შემთხვევაში დაპრინტეთ. თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით ხოლო თუ მიღებული ქულა მეტია 40 ზე და 
#ნაკლებია 70 ზე მაგ შემთხვევაში დაპრინტეთ. თქვენ დაგიფინანსდებათ სწავლა 500 ლარით ხოლო თუ მიღებული ქულა ნაკლებია 40ზე მაგ შემთხვევაში დაპრინტეთ, თქქვენ არ დაგიფინანსდებათ სწავლის პროცესი

score = int(input("ტექსტში რა ქულა მიიღე"))

if 90 <= score <=100:
    print("თქვენ დაგიფინანსდებათ სწავლა სრულიად")
    
if 70 <=score <=80:
    print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით")
    
if 40 <=score <=70:
    print("თქვენ დაგიფინანსდებათ სწავლა 500 ლარით")
    
