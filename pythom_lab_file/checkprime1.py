# def checkprime(n):
#     count = 0
#     for i in range(1,n+1):
#         if n % i== 0:
#          count+=1    
#     if count ==2:
#      print("prime")      
#     else:
#      print("not prime")
    
# b = int(input("enter any number"))        
# checkprime(b)



# print(0.7+0.2==0.9)

# vowels_list = "aeiouAEIOU"
# user_input = input("Enter any string: ")

# vc = 0
# cc = 0

# for i in user_input:
#     # if char.isalpha():  # Check if the character is a letter (ignore spaces/numbers)
#         if i in vowels_list:
#             vc += 1
#         else:
#             cc += 1

# print("Consonants:", cc)
# print("Vowels:", vc)



# def checkprime(n):
#     count = 0
#     for i in range(1,n+1):
#      if i%2 ==0:
#         count+=1
#     if count == 2:
#        print("prime number",n)    
#     else:
#        print("not prime",n)   

# checkprime(6)

def checklatter():        
 vowels = "aeiou"
 user_string = input("enter any string").lower()

 vc= 0
 cc= 0
 for i in user_string:
    if i in vowels:
        vc+=1
    else:
        cc+=1
 print("vowel sting",vc)            
 print("consonant sting",cc)  
checklatter() 
