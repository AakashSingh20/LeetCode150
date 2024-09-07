'''
The trick is that if you take a number and square it up
and create a linked list, at a certain point you will reach 1, in cases when you wont reach 1: you will
actually find that a certain node is reapeated and it will stuck in an endless loop. thats how you detect.

create a hash set for keeping track of visited nums. if the num is already not in set then add it then square
it and if that square is not in the set add it again, keep doing this until you reach 1 or if any two num is
same its a loop and return false.
'''


n = 2

visit = set()
def square(n):
    num = 0
    while n:
        digit = n%10
        digit = digit ** 2
        num += digit
        n = n // 10
    return num

while n not in visit:
    visit.add(n)
    n = square(n)
    if n == 1:
        print(True)
print(False)
