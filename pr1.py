def reverse_print(s):
    if s == "":
        return
    
    reverse_print(s[1:])
    
    print(s[0], end="")


reverse_print("tiger") 