# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:19:40 2023

@author: 91721
"""
#=================================seaborn module==========================
""" seaborn is a visualization library that is built on top of matplotlib
it provides high level interface for drawing attractive and informative 
statistical graphics"""
import seaborn as sns
import pandas
import matplotlib.pyplot as plt

#seaborn has 18 inbuilt datasets
#that can be found by following command
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head()

"""
A count plot is helpful when dealing with categorical values .
it is used to plot the frequency of the different categories
The column sex contains categorical data in the 
 """
sns.countplot(x = 'sex' , data = df)
#x the name of the column
#data - the dataframe 
sns.countplot(x = 'sex'  , hue = 'survived' , data = df , palette = 'Set1')
sns.countplot(x = 'sex'  , hue = 'survived' , data = df , palette = 'Set2')
#hue
#palette

#KDE plot - kernel density estimate used to plot the distribution in continious
#data
sns.kdeplot(x = 'age' , data = df , color = 'black')
#displot
sns.displot(x = 'age' , kde = True , bins = 5 , data = df)
#
sns.displot(x = 'age' , kde = True , bins = 5 , hue = df['survived'] , palette = 'Set1' , data = df)

#Scatter plot
#iris dataset
#iris dataset contains data related to flower's petal size (petal length 
#and petal width) 
#these features are used to classify the type of iris 
#Setosa , versicolor , and virginica
df1 = sns.load_dataset('iris')
#ploting the scatter plot
sns.set_theme()
sns.scatterplot(x='sepal_length' , y = 'petal_length' , data = df1 , hue = 'species')
"""in the plot above we can observe that an iris flower with a sepal
 length <6cm and petal length > 2cm it is most likely of type setosa
Although there is no distinct boundary present between the versicolor 
dot and virginica dot , an iris flower with petal length between 2cm
and 5cm is most likely of type versicolor, while iris flower with petal 
length > 5cm are most likely of type virginica"""

#A join plot
#a joint plot is also used to plot the corelation between
sns.jointplot(x = 'sepal_length' , y= 'petal_length' , data = df1 , kind = 'reg')
sns.jointplot(x = 'sepal_length' , y = 'petal_length' , data = df1 , kind = 'hist')
sns.jointplot(x = 'sepal_length' , y = 'petal_length' , data = df1 , kind = 'kde')
"""kind = kind of plot to be plotted 
it can be one of the following
'scatter' , 'hist' , 'hex' , 'kde' , 'reg' , 'resid """

#pair plot
sns.pairplot(df1)

#A heat map can be used to visualize confusion , matrices
corr = df1.corr()
sns.heatmap(corr)
#============================slot2===================================
"""information of the assignment """
"""columns , describe() , histogram , displot , boxplot """
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
"""data dictionary : information of the columns """
cars = pd.read_csv("C:/1-python/car.csv")
cars.columns
cars.describe()

plt.hist(cars.speed)
sns.displot(x = 'speed' , kde = True , bins = 6 ,data = cars)
""" their are almost 10 cars with the speed limit ranging from 5to10
the maximum no of cars i.e 14 are having speed in between 10 to 15
the second max no of cars i.e 12 are having speed of 20 
no of cars with speed 15to20 and 20 to25 are 8 and 7 respectiveley"""

sns.displot(x = 'dist' , kde = True , bins = 6 , data = cars)
#right leg length is more -->right skwed data
#left leg length is more --> left skwed data
""" the first observation from the displot about the data is that
it has distributed in right skewed manner , 
the cars which are travelling distance of 20to40 kms are the higest 
in number i.e 17"""
#outliers --> calculate median
sns.boxplot(cars.speed)

plt.hist(cars.dist)
sns.boxplot(cars.dist)
#their is one outlier 

#skewness and kurtosis of speed
speed_lst = cars['speed'].tolist()
speed_lst
print('skewness of the speed data is',skew(speed_lst))

print('kurtosis of the speed is ' , kurtosis(speed_lst))

#skewness and kurtosis of distance is 
dist_lst = cars['dist'].tolist()
dist_lst
print('skewnes of the distance data is ' , skew(dist_lst))
print('kurtosis of the distance data is ' , kurtosis(dist_lst))
print(skew(dist_lst , axis=0 , bias = True))

# it signifies distribution is possible 
print(kurtosis(dist_lst , axis = 0 , bias = True))
#it is a playkurtic 

""" take iris dataset and perform all the operations and plots on that dataset"""

#scatter joint square heatmap bar
sns.countplot(x = 'speed' , data = cars )

sns.countplot(x = 'dist' , data = cars , hue = 'speed' , palette="Set1" )

sns.kdeplot(x  = 'speed'  , data = cars , color = "black")

sns.scatterplot(x = 'speed' , y = 'dist' , data = cars)
"""from the plot above we can observe that ,
the speed  of the car increases with increasing distance"""

sns.jointplot(x = 'speed' ,  y='dist' , data = cars , kind = 'reg')
"""inference of jointplot """

sns.pairplot(cars)

corr = cars.corr()
sns.heatmap(corr)

""" from the heat map we see that the black area indicates the high values 
exist between the dist-speed , speed-distance , index-dist , dist-index """

"""Data-dictionary : 
    sepal_length : column specifing the length of the sepal 
    sepal_width : column specifing the width of the sepal
    petal_length : column specifing the length of the petal
    petal_width : column specifing the width of the petal
    species : species (setosa , versicolor , virginica)
    """
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
df1 = sns.load_dataset('iris')
df1
df1.columns
df1.describe()
#histogram
plt.hist(df1.sepal_length)
#displot
sns.displot(x = 'sepal_length' , kde = True , bins = 6 , data = df1)
"""the count of the flowers with sepal length is show alongside from this 
displot , here the maximum count of flowers is for the sepal length 6
sepal_length -----------> count
0to5                       16
5to5.5                     36
5.5 to 6                   38
6.5                        33
7                          21
7.5                        60"""
#countplot
sns.countplot(x ='sepal_length'  , data = df1 , hue = "species" , palette='Set2')
#
