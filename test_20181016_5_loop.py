'''
n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Skaitļi!')
print(n)
'''
'''
#šeit cikls bija bezgalīgs ,jo 5 ir lielāks kā nulle
n = 5
while n > 0:
    print('Lather')
    print('Rise')
print('Dry off')
'''
'''
#Jo nulle ir vienāda ar nulli
n = 0
while n > 0:
    print('Lather')
    print('Rise')
print('Dry off!')
'''
'''
while True:
    line =raw_input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
'''
'''
while True:
    line =raw_input('>')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
'''
'''
for i in [5, 4, 3, 2, 1,] :
    print(i)
print('Blastoff!')
'''
'''
friends = 'Joseph', 'Glenn', 'Sally'
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')
'''
'''
i = 5
print(i)
i = 4
print(i)
i = 3
print(i)
i = 2
print(i)
i = 1
print(i)
print('Blastoff!')
'''
'''
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')
'''
'''
print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('After')
'''
'''
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)
'''
'''
zork = 0
print('Before',zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)
'''
'''
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)
'''
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)
