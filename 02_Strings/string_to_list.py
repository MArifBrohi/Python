S = 'shrubbery'

L = list(S)
print(type(L))
print(L)

L[1] = 'c'

print('After changing at index 1:',''.join(L))

# This is another method to change the valuse of the string
firstName='Arif'
B = bytearray(b'firstName')
B.extend(b'brohi')
name= B.decode()
print(name)
