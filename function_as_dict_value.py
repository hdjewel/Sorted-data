def height_finder():
    return 6 * 12 + 2


d = {'height': (6* 12 + 2)}
print d['height'] 

e = {'height':height_finder}

f = e['height']

print f()