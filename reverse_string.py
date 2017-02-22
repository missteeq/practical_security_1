
def reverse_string(mystring):
    if len(mystring) % 4 == 0:
        return ''.join(reversed(mystring))
    return mystring

print('abcd')
print(reverse_string('abcd'))
print('')
print('python')
print(reverse_string('python'))
