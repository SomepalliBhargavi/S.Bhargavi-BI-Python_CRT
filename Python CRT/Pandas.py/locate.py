#pandas use loc attribute to return one or more specified rows/to locate an element
import pandas as pd
calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)

#refer to the row index:
print(myvar.loc["day1"])

#locate named indexes:
#refer to the named index:
print(myvar.loc["day2"])
