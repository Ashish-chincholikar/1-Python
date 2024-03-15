# -*- coding: utf-8 -*-
"""
Created on Tue May  2 08:08:44 2023

@author: 91721
"""
#to check the version of the any pacakages
import pandas as pd 
pd.__version__

#creating dataframe using list
#passsing the list of list handel to the constructor of the DataFrames 

import pandas as pd

techno = [ ["spark" , 20000 , "30days"] ,
         ["pandas" , 10000 , "40days"]
       ]

df = pd.DataFrame(techno)   # Calling DataFrame constructor on list
#by-default the index are numbers starting from 0 in incremental way
#providing names to the colummns
"""
        0      1       2
0   spark  20000  30days
1  pandas  10000  40days
"""
#index for rows
#column for columns
column_names = ["courses" , "Fee" , "Duration"]
row_label = ["a" , "b"]
df = pd.DataFrame(techno, index = row_label, columns = column_names)
print(df)
"""  courses    Fee Duration
a   spark  20000   30days
b  pandas  10000   40days 
"""
df.dtypes
""" courses     object
Fee          int64
Duration    object
dtype: object
note : object and string are similar referencing"""
#seting custom types to DataFrames
#changing the Datatypes of DataFrames
types = {'courses' :str , 'Fee' : float  , 'Duration' : str}

df.dtypes

#creating Dataframes using dictionary
""" the main advantage of creating a DataFrame using dictionary
over list is that we can easily give the labels to the column of the
DataFrame
however we need to explicitly give the column label and row labels in case of the 
list
"""
import pandas as pd
technologies = {
    'courses' : ["spark" , "Pyspark" , "Hadoop"] ,
    'Fee' : [20000 , 25000 , 26000],
    'Duration' : ['30days' , '40days' , '20days'],
    'Discount' : [1000 , 2300 , 1500]
    }

data_frame = pd.DataFrame(technologies)
print(data_frame)

#convert DataFrame to csv file
#using relative path
data_frame.to_csv('data_file.csv')

#using absoulte path
#make sure to change to forward slash / instead of by default \backslash of windows
data_frame.to_csv('C:/1-python/data_file1.csv')

#create dataframe from csv file
#using absoulte path

dframe = pd.read_csv('C:/1-python/data_file.csv')

#using Relative path
dAframe = pd.read_csv('data_file.csv')

#pandas DataFrame - Basic operations

import pandas as pd
import numpy as np

tech = ({     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas" ,  None , "spark"  ,"python"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , np.nan , 40000 , 2000 ,3040],
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' , '20days' , '' , '50days'],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300 , 1500 ,1000 , 2300]
    })
#DataFrame properties used in EDA exploritary data analysis
#shape
#size
#columns
#column.values
#index
#dtypes
row_lables  = ['r0' , 'r1' , 'r2' , 'r3' , 'r4' , 'r5' , 'r6' , 'r7']
df = pd.DataFrame(tech , index = row_lables)
print(df)
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes
#accessing only one column contents
df['Fee']
#accessing multiple columns 
#use [[]] double brackets
df[['Fee' , 'Duration']]

#select certain rows and assign it to another dataframe
#[rows , colums]

df2 = df[6:]
df
df3 = df[:3]
df3
#accessing certain cell from column 'Duration'
df['Duration'][3]
#substrating specific value from each record of a column

df['Fee'] = df['Fee'] - 500
df['Fee']

#Pandas to manipulate the Dataframe
#Describe DataFrame it is a method which gives 5 number summary
#mean , mode , SD , MAX ,Min
df.describe()

#renames for rows and columns
# dataframe columns

row_lables  = ['r0' , 'r1' , 'r2' , 'r3' , 'r4' , 'r5' , 'r6' , 'r7']
df = pd.DataFrame(tech , index = row_lables)
#Assign new header by setting new columns names
df.columns = ['A' , 'B' , 'C' , 'D']

#rename column Names using rename() method
#row->axis = 0
#column->axis = 1
df = pd.DataFrame(tech , index = row_lables)
df.columns = ['A' , 'B' , 'C' , 'D']

df4 = df.rename({'A' : 'C1' , 'B' : 'C2'} , axis = 1)
df4 = df.rename({'C' : 'C2' , 'D' : 'C3'} , axis = 'columns')
df4 = df.rename(columns = {'A' : 'C1' , 'B' : 'c2'})

# -*- coding: utf-8 -*-
"""
Created on Wed May  3 09:09:02 2023

@author: 91721
"""

import pandas as pd
import numpy as np

technologies = {     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas" , "java" , "spark"  ,"python"] ,
    'Fee' : [2000 , 2500 , 26000 , 10000 , 1000 , 40000 , 2000 ,3040],
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' , '20days' , '' , '50days'],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300 , 1500 ,1000 , 2300]
    }

df = pd.DataFrame(technologies)
print(df.dtypes)
""" 
courses      object
Fee         float64
Duration     object
Discount      int64
dtype: object
"""
#convert all types to best possible types
df2 = df.convert_dtypes()
print(df2.dtypes)
""" 
courses     string
Fee          Int64
Duration    string
Discount     Int64
dtype: object"""
#convert all columns to same type
df = df.astype(str)
print(df.dtypes)
""" 
courses     object
Fee         object
Duration    object
Discount    object
dtype: object"""
#Change type for one or multiple columns
df = df.astype({"Fee" : int , "Discount" : float , "courses" : str , "Duration" : str})
print(df.dtypes)

#converting Datatypes for All columns in a list

df = pd.DataFrame(technologies)
print(df.dtypes)
col = ["Fee" , "Discount"]
df[col] = df[col].astype(float)
print(df.dtypes)
col1 = ["Duration" , "courses"]
df[col1] = df[col1].astype(str)
print(df.dtypes)
#---------------------------------------------------------------------
#ignore error 

df = df.astype({"courses": int} , errors = 'ignore')
print(df.dtypes)

#Generating error

df = df.astype({"courses" : int} , errors = 'raise')

#convert feed column to numeric type
df = df.astype(str)
print(df.dtypes)
df['Discount'] = pd.to_numeric(df['Discount'])
df.dtypes



import pandas as pd
import numpy as np

tech = ({     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas" ,  None , "spark"  ,"python"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , np.nan , 40000 , 2000 ,3040],
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' , '20days' , '' , '50days'],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300 , 1500 ,1000 , 2300]
    })
#DataFrame properties used in EDA exploritary data analysis
#shape
#size
#columns
#column.values
#index
#dtypes
row_lables  = ['r0' , 'r1' , 'r2' , 'r3' , 'r4' , 'r5' , 'r6' , 'r7']
df = pd.DataFrame(tech , index = row_lables)
print(df)
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes

#Drop DataFrame Rows and columns
#Drop rows by lables
#for droping rows with lables dont use [[]] brackets for multiple rows
df1 = df.drop(['r1' , 'r2'])
df1

#Delete Rows by position
row_lables  = ['r0' , 'r1' , 'r2' , 'r3' , 'r4' , 'r5' , 'r6' , 'r7']
df = pd.DataFrame(tech , index = row_lables)
"""
df1 = df.drop(df.index[1, 2])
if we are using more than one index we need to use [[]] 2square brackets
or elese it gives the error --->
 IndexError: too many indices for array: array is 
1-dimensional, but 2 were indexed"""
df1 = df.drop(df.index[[1 , 2 , 3, 4]])
df1

#Delete Rows by Index Range

df1 = df.drop(df.index[2:])
df1

#when you have default indexs for rows
df = pd.DataFrame(technologies)
df1 = df.drop(0)#it will drop the record with row no 0
df1 = df.drop(2)#it will drop the record with row no 2
#other all rows will remain as it is
df1

#for deleting multiple rows when we have default row indexing / lables
#then no need to use [[]] double brackets 
df1 = pd.DataFrame(technologies)
df1 = df.drop([0,3])#it will delete row 0 and row3
df1
#using range function to delete the rows 
df1 = df.drop(range(0 , 2))
df1
#delete the rows 0 , 1 according to the range function

#----------------------------------------------------------------------

import pandas as pd

technologies = ({
                'courses' : ["A" ,"B" , "C" , "D" , "E" , "F" , "G"],
                'Fee' : [1,2,3,4,5,6,7],                
                'Duration' : ['1day' , '2day' , '3day' , '4day' , '5day' , '6day' , '7day']
                })

df = pd.DataFrame(technologies)
print(df)
#Drop Columns by Name
#Drop 'Fee'column

# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:12:46 2023

@author: 91721
"""


import pandas as pd

technologies = ({
                'courses' : ["A" ,"B" , "C" , "D" , "E" , "F" , "G"],
                'Fee' : [1,2,3,4,5,6,7],                
                'Duration' : ['1day' , '2day' , '3day' , '4day' , '5day' , '6day' , '7day']
                })

df = pd.DataFrame(technologies)
print(df)
#Drop Columns by Name
#Drop 'Fee'column
df2 = df.drop(['Fee'] , axis = 1)

df = pd.DataFrame(technologies)
df1 = df.drop(labels=['Fee'] , axis = 1)


df = pd.DataFrame(technologies)
df3 = df.drop(columns = ['Fee'] , axis = 1)

#droping of columns by using index
df = pd.DataFrame(technologies)
df4 = df.drop(df.columns[[1]] , axis = 1)
""" util now we made a copy of the Original DataFrame and performed
operations on it"""
#when we need to make the changes in the original dataframe
# then we use inplace = True
df = pd.DataFrame(technologies)
df.drop(df.columns[[1 , 2]] , axis = 1 , inplace = True)

#drop multiple columns
#1. using label Name
df = pd.DataFrame(technologies)
df2 = df.drop(columns=["courses" , "Fee"] ,axis = 1)
#2 using index
df = pd.DataFrame(technologies)
df2 = df.drop(df.columns[[0,1]] , axis = 1 ) 

#Drop columns using list of Columns
df = pd.DataFrame(technologies)
col = ["courses" , "Fee"]
df2 = df.drop(columns = col , axis = 1)

#--------------------------------------------------------------------
#pandas Select Rows by Index (Position / labels)

import pandas as pd
import numpy as np

tech = ({     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas" ,  None , "spark"  ,"python"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , np.nan , 40000 , 2000 ,3040],
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' , '20days' , '' , '50days'],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300 , 1500 ,1000 , 2300]
    })

row_lables  = ['r0' , 'r1' , 'r2' , 'r3' , 'r4' , 'r5' , 'r6' , 'r7']
df = pd.DataFrame(tech , index = row_lables)

#use of iloc and loc 
""" when we want to access Rows and COlumns with the use of index
we uses iloc 
and when we access rows and columns using the lable we use loc

iloc and loc are not functions
they require [] square brackets
iloc and loc are index and label selection technique

iloc and loc uses the slicing operation on the DataFrame
syntax for iloc
df.iloc[srow : erow , scol : ecol]
"""
df2 = df.iloc[ : ,0 : 2 ]
#first slicing is for rows and second is for columns
#here for first slice returns all the rows
#and second slice returns columns 0 to 1 excluding 2

df = pd.DataFrame(technologies)
df2 = df.iloc[0:2 , :]
#all columns and 0 to 1 rows

#slicing specific rows and specific columns
df = pd.DataFrame(technologies)
df2 = df.iloc[0:2 , 0:2]

#example
df3 = df.iloc[ : , 1:3]

#select row by integer index
#getting row by index
df2  = df.iloc[2]

#select row by index list
df2 = df.iloc[[2,3,6]]

#select row by integer index range
df2 = df.iloc[1:5]
#select first row
df2 = df.iloc[:1]
#select first 3 rows
df2 = df.iloc[:3]
#select last row
df2 = df.iloc[-1:]
#select last 3 rows
df2 = df.iloc[-1:-4:-1]
#select alternate rows
df2 = df.iloc[::2]

#-------------------------------------------------------------------

import pandas as pd
import numpy as np

tech = ({     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas" ,  None , "spark"  ,"python"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , np.nan , 40000 , 2000 ,3040],
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' , '20days' , '' , '50days'],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300 , 1500 ,1000 , 2300]
    })

row_lables  = ['r0' , 'r1' , 'r2' , 'r3' , 'r4' , 'r5' , 'r6' , 'r7']
df = pd.DataFrame(tech , index = row_lables)

#use of loc for accessing the rows using the label name
#select rows by lables

df2 = df.loc['r2']#single row using lables
df2 = df.loc[['r2' , 'r3' , 'r6']]#selecting multiple row using lables
#use [[]] brackets
"""when we use slicing with loc using the row lables
then it provides all the rows from start label to end lable
however when we use the slicing with loc using integer index
it provides the rows from start to one less than the last provided 
index value

df.iloc[1:5]-->1,2,3,4
df.loc['r1' : 'r5']-->r1,r2,r3,r4,r5  """
df2 = df.loc['r1' : 'r5']
df2 = df.loc['r1' : 'r5' : 2]

#selecting columns
#loc[] syntax to slice columns
#df.loc[: , start:end:step]

#select multiple columns
#df.loc[srow:erow:step ,scol:ecol:step]-->[rows , columns]
df2 = df.loc[ : , ["courses" , "Fee" , "Duration"]]
#select Random Columns
df2 = df.loc[: , ["courses" , "Duration"]]
#select columns between two columns
df2 = df.loc[: , "Fee" : "Duration"]
#selecting columns by range
#all columns from Duration to end
df2 = df.loc[: , 'Duration' : ]


#All the Columns upto "Duration"
df2 = df.loc[: , : "Duration"  ]

#Pandas.DataFrame.query() by Examples
#Query All rows with COurses equalt to "spark"

df2 = df.query("courses == 'spark'")
print(df2)
df2 = df.query("Fee == 2000")
print(df2)

#not equal condition
#all the rows which does not include spark
df2 = df.query("courses != 'spark'")
print(df2)

#----------------------------------------------------------------
import pandas as pd
import numpy as np

tech = {     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas" ,  None , "spark"  ,"python"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , np.nan , 40000 , 2000 ,3040],
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' , '20days' , '' , '50days'],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300 , 1500 ,1000 , 2300]
    }

df = pd.DataFrame(tech)
#Adding columns to the DataFrame

# -*- coding: utf-8 -*-
"""
Created on Fri May  5 08:21:48 2023

@author: 91721
"""

#pandas add column to DataFrame
import pandas as pd
import numpy as np
tech = ({     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , 6000] , 
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' ],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300]
    })

df = pd.DataFrame(tech)

tutors = ['ram' , 'shyam' , 'ramesh' , 'ganesh' , 'ganesh']
#Add new column to DataFrame

df2 = df.assign(TutorsAssigned = tutors)

#Adding multiple columns in the dataFrame
mnc = ['A' , 'B' , 'C' , 'D', 'E']
df2 = df.assign(mnc_comp = mnc , TutorsAssigned = tutors)  
df2

#how to derive new column from existing column
df = pd.DataFrame(tech)
df2 = df.assign(discount_per = lambda x : x.Fee * x.Discount /100)

#appending new column to the exisiting DataFrame
df["MNC_comp"] = mnc#-->frequently used simple syntax

#Adding columns at specified location
#to add the new columns at the starting is of importance while
#working on Machine learning
df = pd.DataFrame(tech)
df.insert(0 , "TUTORS" , tutors)

#---------------------------------------------------------
#pandas add column to DataFrame
import pandas as pd
import numpy as np
tech = ({     
    'courses list' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , 6000] , 
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' ],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300]
    })

df = pd.DataFrame(tech)
df.columns
df.rename(columns  = {'courses list' : 'courses_list'},inplace = True)
df.rename(columns  = {'Fee' : 'FEE' , 'Duration'  : "DURATION" , 'Discount' : "DISCOUNT"},inplace = True)

#
df2 = df.rename({'courses list' : 'courses_list'} , axis =1)


# -*- coding: utf-8 -*-
"""
Created on Mon May  8 08:24:33 2023

@author: 91721
"""


import pandas as pd
import numpy as np
tech = ({     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , 6000] , 
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' ],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300]
    })

df = pd.DataFrame(tech)

#get the number of rows in DataFrame

row_count = len(df.index)
row_count
row_count = len(df.axes[0])
row_count

df.shape[0]#-->number of rows
df.shape[1]#-->number of columns

df.shape#-->(rows , columns)

#pandas apply Function to a column
import pandas as pd
import numpy as np

data = {
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]
        }

df = pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
#to apply any function to the DataFrame 
# df.apply(function_name)-->to entire DataFrame
df2 = df.apply(add_3)
print(df2)

#apply function to a single column

data = {
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]
        }

df = pd.DataFrame(data)
print(df)

def add_4(x):
    return x+4

df["B"] = df["B"].apply(add_4)
df["B"]
#apply function to multiple columns

df[["A","B"]] = df[["A" , "B"]].apply(add_4)
df[["A" , "B"]]

#Apply lambda function to each column in DataFrame

df2 = df.apply(lambda x : x+10)
df2 
#Apply lambda function to a single column in DataFrame

df["A"] = df["A"].apply(lambda x : x+10)
df['A']

#Applying function to DataFrame or column using the Transform method
import pandas as pd
import numpy as np

data = {
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]
        }

df = pd.DataFrame(data)
def add_2(x):
    return x+2
df2 = df.transform(add_2)
df2

#Applying funciton using map() function
data = {
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]
        }

df = pd.DataFrame(data)
def add_2(x):
    return x+2
df["A"] = df["A"].map(add_2)
df

#numpy Module in python

import numpy as np
data = {
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]
        }

df = pd.DataFrame(data)
print(df)
df["A"] = df["A"].apply(np.square)
print(df)
#using the numpy.square() function

df["A"] = np.square(df["A"])
df

#pandas groupby() with example
#when their are repeated entities in a column we can group them
import pandas as pd
import numpy as np
tech = ({     
    'courses' : ["spark" ,"Hadoop" , "Pyspark" , "Hadoop" , "python" , "pandas" , "python"] ,
    'Fee' : [20000 , 25000 , 2000 , 26000 , 10000 , 6000 , 8000] , 
    'Duration' : ['30days' , "20days" , '40days' , '20days' ,'30days' , '40days' , '10days' ],
    'Discount' : [1000 , 2300 , 1000 , 1500 ,1000 , 2300 , 1000]
    })

df = pd.DataFrame(tech)

df2 = df.groupby(['courses']).sum()
print(df2)

#Group Multiple Columns

df2 = df.groupby(['courses' , 'Duration']).sum()
print(df2)

#Add row index to the group by result
df3 = df.groupby(['courses' , 'Duration']).sum().reset_index()
print(df3)

#------------------------Evening------------------------------
#get column names from DataFrame
import pandas as pd
import numpy as np
tech = ({     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , 6000] , 
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' ],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300]
    })

df = pd.DataFrame(tech)
df.columns

#using list(df) to get column header in list
columns_header = list(df.columns.values)
columns_header


columns_header = list(df.columns)
columns_header


columns_header = list(df)
columns_header

#Pandas shuffle DataFrame Rows
#shuffling of rows
import pandas as pd
import numpy as np
tech = ({     
    'courses' : ["spark" , "Pyspark" , "Hadoop" , "python" , "pandas"] ,
    'Fee' : [20000 , 25000 , 26000 , 10000 , 6000] , 
    'Duration' : ['30days' , '40days' , '20days' ,'30days' , '40days' ],
    'Discount' : [1000 , 2300 , 1500 ,1000 , 2300]
    })

df = pd.DataFrame(tech)
print(df)

df1 = df.sample(frac=1)

#creating a new index starting from zero
df1 = df.sample(frac=1).reset_index()
df1

#in order to remove the holder index
df2 = df.sample(frac = 1).reset_index(drop = True)
df2

#--------------------------Assignment-----------------------
import pandas as pd
import numpy as np

df = pd.read_csv("Company_Data.csv")
df

#Get the number of Rows in the df 
rows_count = len(df.index) 
print(rows_count)

rows_count = len(df.axes[0])
print(rows_count)

rows_count = df.shape[0]
print(rows_count)

#Applying function on the columns of a DataFrame
def add_100(x):
    return x+100

print(df['CompPrice'])

df1 = df['CompPrice'].apply(add_100)
print(df1)

df2 = df[['CompPrice','Population']].apply(add_100)
df2

#Instead of apply we can also use transform
df0 = df['Age'].transform(add_100)

#using lambda function 
df3 = df['Age'].apply(lambda Age:Age+10)

#using df.map() to single column
df['Age'] = df['Age'].map(lambda Age:Age+5)
print(df['Age'])

#using numpy function to a single column through pandas
df['Sales'] = df['Sales'].apply(np.square)
df['Sales']

df = np.square(df['Sales'])

#use groupby to complete the sum()

df = pd.read_csv("Company_Data.csv")
df

df4 = df.groupby(['ShelveLoc']).sum()
df4

# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:23:31 2023

@author: 91721
"""
#joining 

import pandas as pd

technologies = {
    'Courses' : ["Spark" , "Pyspark" , "Python" , "Pandas"],
    'Fee' : [2000 , 3000 , 2500 , 1500],
    'Duration' : ["20days" , "30days" , "40days" , "25days"]
   }

index_lables = ['r1' , 'r2' , 'r3' , 'r4']
df1 = pd.DataFrame(technologies , index = index_lables)
print(df1)

technologies2 = {
        'Courses' : ["Spark" , "Pyspark" , "Python" , "Pandas"],
        'Discount' : [100 , 200 , 400 ,200]
    }

index_lables2 = ['r1' , 'r6' , 'r3' , 'r5']
df2 = pd.DataFrame(technologies2 , index = index_lables2)
print(df2)
"""
DataFrame1 
    Courses   Fee Duration   
r1    Spark  2000   20days 
r2  Pyspark  3000   30days
r3   Python  2500   40days
r4   Pandas  1500   25days

DataFrame2 
     Courses  Discount
 r1    Spark       100
 r6  Pyspark       200
 r3   Python       400
 r5   Pandas       200

"""
#bydefault left join is performed
df3 = df1.join(df2 , lsuffix = "_left" , rsuffix = "_right")
print(df3)
""" 
left join
Courses_left      Fee   Duration    Courses_right  Discount
r1        Spark  2000   20days         Spark     100.0
r2      Pyspark  3000   30days           NaN       NaN
r3       Python  2500   40days        Python     400.0
r4       Pandas  1500   25days           NaN       NaN"""
#how parameter defines how we have to join the DataFrames
#how = 'inner' performs innerjoin on DataFrame
df4 = df1.join(df2 , lsuffix = "_left" , rsuffix = "_right" ,how = 'inner')
print(df4)
"""
inner join
   Courses_left   Fee Duration Courses_right  Discount
r1        Spark  2000   20days         Spark       100
r3       Python  2500   40days        Python       400 """

#right join
df5 = df1.join(df2 , lsuffix = "_left" , rsuffix = "_right" ,how = 'right')
print(df5)

""" 
RIGHT JOIN
 Courses_left     Fee Duration Courses_right  Discount
r1        Spark  2000.0   20days         Spark       100
r6          NaN     NaN      NaN       Pyspark       200
r3       Python  2500.0   40days        Python       400
r5          NaN     NaN      NaN        Pandas       200"""

#pandas merge DataFrame
technologies = {
    'courses' : ["Spark" , "Pyspark" , "Python" , "Pandas"],
    'Fee' : [2000 , 3000 , 2500 , 1500],
    'Duration' : ["20days" , "30days" , "40days" , "25days"]
   }

index_lables = ['r1' , 'r2' , 'r3' , 'r4']
df1 = pd.DataFrame(technologies , index = index_lables)
print(df1)

technologies2 = {
        'courses' : ["Spark" , "Pyspark" , "Python" , "Pandas"],
        'Discount' : [100 , 200 , 400 ,200]
    }

index_lables2 = ['r1' , 'r6' , 'r3' , 'r5']
df2 = pd.DataFrame(technologies2 , index = index_lables2)
print(df2)

#--------------------slot2---------------------------------------
#pandas join the column by inner join
df3=df1.set_index('courses').join(df2.set_index('courses'),how='inner')
df3
##################
#pandas join the  column by left join
df3=df1.set_index('courses').join(df2.set_index('courses'),how='left')
df3
####################
#pandas join the column by right join
df3=df1.set_index('courses').join(df2.set_index('courses'),how='right')
df3
##############################
"""import pandas as pd
tech1={
       'courses':['spark','pyspark','python ','pandas'],
       'fee':[2134,3456,4567,768],
       'duration':['34days','54days','43days','36days'],
       'discount':[2134,3456,45367,5635]
        }

index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(tech1,index=index_labels)
df1
tech2={
       'courses':['spark','java','python ','go'],
       'discount':[2134,3456,4567,565]
        }

index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(tech2,index=index_labels2)
df2"""
#if you want to excecte this code you  can use the  above commentted dataframe
#we can join(use any join i.e. left ,right or inner)
# the more than one colummn by using the doble coat and [] bracket
df3=df1.set_index(["courses","discount"]).join(df2.set_index(["courses","discount"]),how='right')
df3


#################################
# inner join is as same as merge concept
#pandas merge dataframe
import pandas as pd
tech1={
       'courses':['spark','pyspark','python ','pandas'],
       'fee':[2134,3456,4567,768],
       'duration':['34days','54days','43days','36days']
        }

index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(tech1,index=index_labels)
df1

tech2={
       'courses':['spark','java','python ','go'],
       'discount':[2134,3456,4567,565]
        }

index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(tech2,index=index_labels2)
df2
#creation of the dataframe 
############################
#using the pandas merge()
df3=pd.merge(df1,df2)
df3
"""Out[33]: 
   courses   fee duration  discount
0    spark  2134   34days      2134
1  python   4567   43days      4567"""
#it can give the out put   by default left join and 
#merge() concept work as the inner join
# it is going to join on the inddex
###########################
#using the dataframe merge()
df3=df1.merge(df2)
df3


##############
# join the datframe horizontaly
#use pandas concat() to  concat to the datafrme
import pandas as pd
df=pd.DataFrame({
    'courses':["python","haddop","typ","gtu"],
    'fees':[3456,43235,675,567]})
df1=pd.DataFrame({
    'courses':["pyty","hadd","yp","tu"],
    'fees':[346,435,75,67]})

################
#use pandas concat() to  concat to the datafrme
data=[df,df1]
df2=pd.concat(data)
df2 
# it give the doble index  value ie from 0 and 2nd also 0
"""Out[41]: 
  courses   fees
0  python   3456
1  haddop  43235
2     typ    675
3     gtu    567
0    pyty    346
1    hadd    435
2      yp     75
3      tu     67"""


################################
## concat () the more or multiple dtaframe using the ppandas  concat()
import pandas as pd
df=pd.DataFrame({
    'courses':["python","haddop","typ","gtu"],
    'fees':[3456,43235,675,567]})
df1=pd.DataFrame({
    'courses':["pyty","hadd","yp","tu"],
    'fees':[346,435,75,67]})
df2=pd.DataFrame({
    'Duration':["45days","56days","23days","78days"],
    'discount':[346,435,75,67]})

# concat () the more or multiple dtaframe using the ppandas  concat()
df3=pd.concat([df,df1,df2])
print(df3)
#################################
# write to create the dataframe by csv file by default
#when  we want to create the file taht time must need ,
#to give the absulte path not the relative path
df3.to_csv("C:/Data Science/1-python/courses.csv")
# it is use to create the csv file inghe give in folder

###############
# read csv file into the dataframe
# read the csv file we give the relative path or absulte path
df=pd.read_csv('courses.csv')
df


##########################
#write dataframe to the excel file
#creation of excel file
df3.to_excel("C:/Data Science/1-python/courses.xlsx")

##############################
#read the excel file
import pandas as pd
df=pd.read_excel("C:/Data Science/1-python/courses.xlsx")
df

# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:26:34 2023

@author: 91721
"""

import pandas as pd
songs2 = pd.Series([145 , 142 , 38 ,13],name = 'counts')
#it is easy to inspect the index of a series (or DataFrame)
songs2.index

#changing the index of the Series
songs3 = pd.Series([145 , 142 , 38 , 13], name = 'counts' , 
                   index = ['ram' , 'suresh' , 'vinod' , 'mahesh'])

#The NULL values 
#Stands for 

#finding the mean values
songs2 = pd.Series([145 , 142 , 38 ,13],name = 'counts')
songs2.mean()

#duplicate index values can be present

george = pd.Series([10 , 20 , 30 , 40 ] ,
         index = ['1' ,'2' ,'3' , '3'] ,
                   name = 'George_songs')
george

#read the data from the series
george['2']

#we can iterate over data in a Series
for item in george:
    print(item)
    
#updating values in Series
george['2'] = 200
george
#the values at the index label 2 is update to 200 from 20

#deletion 
s = pd.Series([2,3,4] , index = [1,2,3])
s
del s[1]
s
#for duplicate index labels , the values for all the duplicates will be deleted
del george['3']
george
#the value at the specified index/indexlables is deleted 
#problems with duplicate index

#converting values / datatypes
#string uses .astype(str)
#integer uses pd.to_numeric
songs_66 = pd.Series([3, None , 11 , 9] , index = ['A' , 'B' , 'C' , 'D'],
                     name = 'counts')

pd.to_numeric(songs_66.apply(str))
#this will give error , unable to parse string "nan"
#to overcome this error we specify the parameter error = 'coerce'
pd.to_numeric(songs_66.apply(str) , errors = 'coerce')

#fill the All the NULL values with -1 
songs_66.fillna(-1)

#drop the NULL Values
songs_66.dropna()

#Append , combining and joining two series
songs_69 = pd.Series([ 7 ,16 , 21 ,39] , index = ["ram" , "shyam" , "ghansham" , "krishna"] , 
                     name = "counts")

songs = songs_66.append(songs_69)
songs

#---------------------matplot Module----------------------------------
import matplotlib.pyplot as plt

fig = plt.figure()
songs_69.plot()
songs_69.plot()
plt.legend()
###################################
#-------------------------bar graph--------------------------------
fig = plt.figure()
songs_69.plot(kind = 'bar')
songs_69.plot(kind = 'bar' , color = 'k' , alpha=.5)
plt.legend()
###################################
#--------------------------histogram-----------------------------
import numpy as np
data = pd.Series(np.random.randn(500) , name = '500 random')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()
