string = input("Enter a non-empty string: ")


n = int(input("Enter the index of the character to remove: "))


if n < 0 or n >= len(string):
    print("Index out of range")
else:
    
    modified_string = string[:n] + string[n+1:]
    print("Original String:", string)
    print("Modified String:", modified_string)
