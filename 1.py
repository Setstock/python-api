string = str(input("Enter the world: "))
rev_string = string[ : : -1]
print("reversed world: ",rev_string)
if string == rev_string:
    print("World is palindrome")
else:
    print("World isn't palindome")

