#data frames-has more than 1 coloumn or series/multidimensional tables
import pandas as pd
Data={
    'Std1':
    {'Name':'Rose',
    'Branch':'Bioinformatics',
    'ID':1001,
    'Skills':['Python','C','SQL']
    },
    'Std2':
    {'Name':'Jack',
    'Branch':'Bioinformatics',
    'ID':1002,
    'Skills':['Python','DSA','SQL']
    }
}
Data=pd.DataFrame(Data)
print(Data)
print(type(Data))