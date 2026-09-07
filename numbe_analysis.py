 
n = int(input("Enter a number (n): "))
total_sum = 0
even_sum = 0
odd_sum = 0

print("\nNumbers and their types:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} - Even")
        even_sum += i  
    else:
        print(f"{i} - Odd")
        odd_sum += i   
        
    total_sum += i  
print("\n--- Results ---")
print("Sum of all numbers:", total_sum)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

if total_sum % 2 == 0:
    print("Total sum is Even")
else:
    print("Total sum is Odd")