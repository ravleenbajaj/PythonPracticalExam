def string_menu():

    ch =int(input('''Choose your function:
1. Length of string
2. Maximum of three strings
3. Accept a string and replace every successive character with ‘#’ Example- For Given string ‘Hello World’ returned string is ‘H#l#o W#r#d’.
4. Number of words in the given string
5. Exit
'''))
    if ch == 1:
        n = input("Enter a string : ")
        l=len(n)
        print("The length of the string is =",l)      
    elif ch == 2:
        n1 = input("Enter 1st string : ")
        n2 = input("Enter 2nd string : ")
        n3 = input("Enter 3rd string : ")
        print("The maximum of the three strings is =",max(n1,n2,n3))    
    elif ch == 3:
        n = input("Enter a string : ")
        s = ""
        m = list(n)
        for i in range(len(n)):
            if (i%2 != 0):
                if m[i] == " ":
                    m[i] = " "
                else:
                    m[i] = "#"
        for x in m:
            s=s+x
        print("The sucessive character in the string is replaced with # :",s) 
    elif ch == 4:
            n = input("Enter a string : ")
            c = 0
            for y in n :
                if y == " " :
                    c += 1
            w = c+1
            print("The number of words = ",w) 
    else :
        print("Incorrect option, try again!")
        
while True:
    string_menu()