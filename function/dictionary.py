#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']",dict['Name'])
print("dict['Age']", dict['Age'])

# updating existing entry
dict['Age'] = 8
# Add new entry
dict['school'] = 'DPS School'
print(dict['school'])

# Delete Dictionary Elements
del dict['school']  # remove entry with key 'Name'
dict.clear()        # remove all entries in dict
del dict            # delete entire dictionary

# some properties of Dictionary Keys
# (a) more than one entry per key not allowed.
# when duplicate keys encountered during assignment
# the last assignment wins
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print("dict['Name']", dict['Name'])
# (b) Keys must be immutable. Which means
# you can use strings, numbers or tuples as
# dictionary keys but something like ['key'] is not allowed
