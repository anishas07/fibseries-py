def fibseries(n):
    a, b = 0, 1  
    count = 0
    while count < n:  
        print(a, end=' ')
        a, b = b, a + b
        count += 1  


n = int(input("how many times do you want to repeat the Fibonacci series? "))
if n <= 0:
    print("Make sure the number is postive, since it doesnt work negative numbers.")
else:
    fibseries(n)