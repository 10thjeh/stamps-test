# INSTRUCTIONS:
# Please create an array/list of numbers from 1 to 100. Print all these numbers in reverse order, but with the following rules :

# Do not print prime numbers.
# Replace numbers divisible by 3 with the text "Foo."
# Replace numbers divisible by 5 with the text "Bar."
# Replace numbers divisible by both 3 and 5 with the text "FooBar."
# Print the numbers horizontally, not vertically.
import math

def isPrime(x):
    if x <= 1:
        return False
    return not any([x%n == 0 for n in range(2, x)])

def fizzbuzz():
    nums = [x for x in range(1,101) if not isPrime(x)][::-1]
    ans = []
    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            ans.append("FooBar")
        elif num % 3 == 0:
            ans.append("Foo")
        elif num % 5 == 0:
            ans.append("Bar")
        else:
            ans.append(str(num))

    return ', '.join(ans)

print(fizzbuzz())