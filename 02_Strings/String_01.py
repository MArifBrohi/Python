S = 'Spam'

# we can verify its length by using built-in function
print(f'length of string {len(S)} ')

print(S[0])

print(S[1:-1]) #starts with index 1 to 3 but not included 3 index
#output: pa 

print(S[-1])
#output: m

# negative indexing
print(S[len(S)-1])

print(S[0:5])  # 0 to 4 but 5 not included
#output: Spam 

#using concatination but it make a copy 
print( S+'xyz')
#output: Spamxyz

# S is unchanged
print(S)
#output: Spam

# Repetition
print(S*4)