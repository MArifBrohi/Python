'''
Strings are immutabile in Python that whenever we were chagning the 
orignal string were not changing actually. Every String produce a new 
String as its result. They can not be changed in place after they are 
created.
'''
S = 'Spam'
S[0] = 'E'
print(S)

'''output:  Traceback (most recent call last):
  File "d:\Coding World\Python\Strings\String_02_Immutability.py", line 8, in <module>
    S[0] = 'E'
    ~^^^
TypeError: 'str' object does not support item assignment

===========================================================
Numbers, strings and tuples are immutable;
lists, dictionaries and sets are mutable they can be changed freely


'''