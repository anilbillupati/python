def greet():
    print("Hello, World!")

def print_even_numbers( n ):
    for i in range(n):
        if i % 2 == 0:
            print(i)

print_even_numbers(int(input("enter the number:"))) 