
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

s5 = r"spam\n"


print("Guido's the guy!")

print('Guido is the "BDFL" of the Python world')

print("""Guido's the "BDFL" of Python""")

# print("Guido's the \"BDFL\" of Python")

print(r"Path is c:\stuff\trash")

actor = "Chris Hemsworth"
print(actor)

print(type(actor))

a = actor.upper()
print(a)

print(actor.upper())

print(actor.replace('H', 'P'))

print(actor.replace('Hem', 'Penny'))
print(actor.replace('Hem', ''))

print(actor.count('h'))
print(actor.count('H'))

print(actor.lower().count('h'))
print(actor.lower().count('h'))

info = "National Grid:1 Latti Rd:Milbury:MA"

fields = info.split(':')

print(fields)
print(info.split(':')[0])

print(','.join(fields))

poem = "Roses    are     red"

words = poem.split()

print(words)

print(actor.index('em'))
print(actor.find('x'))
print(actor.rindex('h'))
print(actor.find('em'))
print()
pos1 = actor.index('h')
print(pos1)
pos2 = actor.index('h', pos1 + 1)
print(pos2)
print()

s1 = "       All my exes live in Texas        "

print('|' + s1.lstrip() + '|') # space tab \n \r \f \b
print('|' + s1.rstrip() + '|')
print('|' + s1.strip() + '|')
print()

s2 = "xyxyxxxyyyyxyxyxxAll my exes live in Texasyyyxxxyxyxyyyyyyyyy"

print('|' + s2.lstrip('xy') + '|')
print('|' + s2.rstrip('xy') + '|')
print('|' + s2.strip('xy') + '|')
print()





