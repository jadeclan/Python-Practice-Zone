for i in range(0,11):
    print(f'{i},  {i**2}')

name = 'james'
print(name == 'James')          # Expecting false
print(name=='james'.lower())    # Expecting true

name = ('james', 'bergeron')    # A tuple

print(name[0].title())
print(name)