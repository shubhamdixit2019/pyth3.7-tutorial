''' Tuples have parenthesis but lists do have square brackets like an array  '''
numbers = (1,5,4)
'''This will thow error as lists values can be changes but not that of a tuple 
removve the below linee else face error numbers[0]=10'''
x,y,z = numbers
print(x,y,z)
