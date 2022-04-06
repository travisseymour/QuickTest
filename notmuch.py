import string

print('This Change Is Gonna Fail!')

print('============================')
print('==  Welcome to QuickTest  ==')
print('============================')
print()
for i, c in enumerate(string.ascii_lowercase):
    print(f"{i}. lower={c} upper={c.upper()}")

for i in range(10):
    print(i, end='...')

print()
print('All Done!! 🐮🔔')
print('^^^^^^^^^^^^^^^')