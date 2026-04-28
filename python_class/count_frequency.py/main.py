import frequency
string =  input("enter any charector:")
result = frequency.count_frequency(string)
print("frequency in your string ")
for key,value in result.items():
    print(key,":",value) 