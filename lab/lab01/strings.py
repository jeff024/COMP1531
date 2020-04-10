'''
TODO Complete this file by following the instructions in the lab exercise.
'''

strings = ['This', 'list', 'is', 'now', 'all', 'together']
string = ""

for word in strings[:-1]:
    string += word
    string += ' '
string += strings[-1]

print(string)
#print(' '.join(strings))
