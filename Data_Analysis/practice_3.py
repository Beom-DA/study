#



import pandas as pd

'''series = pd.Series(['banana', 42])
print(series)

s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)'''

'''scientists = pd.DataFrame({ 
    'Name': ['Rosaline Franklin', 'William Gosset'], 
    'Occupation': ['Chemist', 'Statistician'], 
    'Born': ['1920-07-25', '1876-06-13'], 
    'Died': ['1958-04-16', '1937-10-16'], 
    'Age': [37, 61]}) 
print(scientists)'''

'''from collections import OrderedDict #순서보장 딕셔너리
scientists = pd.DataFrame(OrderedDict([ 
    ('Name', ['Rosaline Franklin', 'William Gosset']),
    ('Occupation', ['Chemist', 'Statistician']), 
    ('Born', ['1920-07-25', '1876-06-13']), 
    ('Died', ['1958-04-16', '1937-10-16']), 
    ('Age', [37, 61])
])
) 
print(scientists)'''


scientists = pd.DataFrame( 
    data={'Occupation': ['Chemist', 'Statistician'], 
          'Born': ['1920-07-25', '1876-06-13'], 
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Age', 'Died'])  #columns 열 순서가 유지된다.
print(scientists)