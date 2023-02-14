def max_num(a, b, c):
    return max(a, b, c)
    
    
print(max_num(1, 4, 5))



numbers = [1, 2, 3, 4, 5]

def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
print (mult_list(numbers))

string = "hello"
def rev_string(string):
    return string[::-1]

print(rev_string(string))

def num_within(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

# Test the function
num = 5
start = 1
end = 10
result = num_within(num, start, end)
if result:
    print(f"{num} is within the range {start} to {end}")
else:
    print(f"{num} is not within the range {start} to {end}")


def pascal(n):
    row = [1]
    for i in range(n):
        print(*row)
        row = [x + y for x, y in zip([0]+row, row+[0])]

# Test the function
pascal(5)
