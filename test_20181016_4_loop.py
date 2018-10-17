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
while True:
    line =raw_input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

