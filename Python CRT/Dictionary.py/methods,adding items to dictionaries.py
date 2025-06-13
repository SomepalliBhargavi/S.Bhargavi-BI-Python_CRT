JobRole={101:'Full Stack Developer',102:'Data Engineer',103:'Data Analyst',104:'Data Scientist'}
print(JobRole)
JobRole[105]='Cloud Engineer'
JobRole[106]='Power BI analyst'
JobRole[107]='web developer'
print(JobRole)

#remove an item
JobRole.pop(101)
print(JobRole)

#removing an item using del keyword
del JobRole[103]
print(JobRole)

#len() dictionary operations
print(len(JobRole))

#Keys() -returns a list if keys
print(JobRole.keys())

#Values() - returns a list of values
print(JobRole.values())

#items() -returns a list of key-value pairs(tuples)
print(JobRole.items())

#copy() - returns copy of the dictionary
b=JobRole.copy()
print(b)





















