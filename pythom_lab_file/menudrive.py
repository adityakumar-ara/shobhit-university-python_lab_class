string = input("enter any string: ")
while(1):
   print("Enter 1. for find frequncy of character in string")
   print("Enter 2. replace charater another charector")
   print("Enter 3. remove first of character in string")
   print("Enter 4. remove all charater in string")
   print("Enter 5, for exit")
   a = int (input("Choose an option:"))
   if a == 1:
    s = input("enter count word in string")
    print(string.count(s))
   elif a==2:
    s = input("enter word who want to replace")
    m = input("enter new word")
    print(string.replace(s,m))   
   elif a == 3:
    print(string[1:])
   elif a == 4 :
    new_str = string[:]
    string = "" 
    print("String cleared:", string)
   elif a == 5:
    print("Exiting....")
    break
   else:
      print("Inviled input")
      