# clockwise program
print('clock program')

s = 'CAR'
l = list(s)
print(l)
l.append(l.pop(0))
print(''.join(l))

# Output --> ARC

# Clockwise to print all Iterations

print('Clockwise string program')

s = 'BIKE'
l = list(s)
print(l)
for i in range(0,len(s)):
    l. append(l.pop(0))
    print(''.join(l))



# WAP Anti-clock

# a = 'CAR'
# b = list(a)
# l.insert(0,b.pop(-1))
# print(''.join(b))

