'''
travese from the back and add 1 to the last digit, if the sum is 10 then change the digit to 0 and 
move on to the next num, if in a case the i pointer reaches the beginning then add 1 to the array.
'''


digits = [9,9,9]

for i in range(len(digits)-1,-1,-1):
    if digits[i] + 1 != 10:
        digits[i] += 1
        print(digits)
        break

    digits[i] = 0

    if i == 0:
        digits = [1] + digits
        print(digits)
        break
