# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]

    item = l.pop()
    return item * multiply_list(l)

#print multiply_list(range(1, 5))    


# Return the factorial of n
def factorial(n):
    total = 1
    if n == 1:
        return 1
    else:
        total = factorial(n-1)*n
    return total

# Count the number of elements in the list l
def count_list(l):
   
    if len(l) == 1:
        return 1
    l.pop()
    return 1 + count_list(l)


# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return 1

    item = l.pop()
    return item + sum_list(l)

#print sum_list([1, 2, 3, 4])


# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l
    
    item = [l.pop()]
    new_list = reverse(l)
    return item + new_list

    #item = l.pop()
    #return [item] + reverse(l)

#print reverse([10,5,2,1])

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(5)


# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    item = l.pop()
    if item == i:
        return item
    if len(l) == 0:
        return None
    else:
        return find(l, i)


# Determines if a string is a palindrome
def palindrome(some_string):
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target. Call by count_up(100, 0)
def count_up(target, n):
    return
