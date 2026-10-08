count = 1
total = 0

# BUG: The while condition was missing its required colon, so Python could not parse the loop.
# BUG: The loop stopped before adding 5 because count < 5 excluded the final number.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The total was concatenated with a string instead of converted to a string.
print("Sum of 1 to 5 is: " + str(total))
