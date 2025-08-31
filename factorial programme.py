def a(n) :
    if n < 2 :
        return 1
    else:
        return (n * a (n-1))
     
# x = a(8)
x = a (int(input("enter a no")))    
print(x)