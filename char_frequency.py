import collections

#def char_frequency(mystring):

text = 'google.com'
char_frequency = collections.Counter(text)

"""dict = {}
    for n in mystring:
        keys = dict.keys()        
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict"""

print(char_frequency.most_common())
