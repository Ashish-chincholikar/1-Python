
#============================================================
import matplotlib.pyplot as plt
plt.__version__

plt.plot([1,2,3,4])
plt.show()

#multiline plots
x = range(1 , 5)

plt.plot(x , [xi*1.5 for xi in x])
plt.plot(x , [xi*3.0 for xi in x])
plt.plot(x , [xi/3 for xi in x])

plt.show()

#grid , axes and lables

import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(1, 5)
plt.plot(x , x*1.5 , x , x*3.0 , x , x/3)
plt.grid(True)
plt.show() 

#handling axes

import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(1, 5)
plt.plot(x , x*1.5 , x , x*3.0 , x , x/3)

plt.axis()#shows the current axis limits values

plt.axis([ 0 , 5 , -1 , 13]) # set new axis limits
#[xmin , xmax , ymin , ymax]

plt.show()

#Adding lables
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel('This is my x label')
plt.ylabel("this is my y label")
plt.show()

#Adding a title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title("SIMPLE PLOT")
plt.show()

#Adding legend
import matplotlib.pyplot as plt
import numpy as np

plt.plot(x , x*1.5 , label = 'Normal')
plt.plot(x , x*3.0 ,label = "Fast")
plt.plot( x , x/3 , label = "slow")
plt.legend()
plt.show()

#control colours
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1,3)
plt.plot(y , 'y')
plt.plot(y+1 , 'm')
plt.plot(y+2 , 'c')
plt.show()

#specifiying styles in multiline plot
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1,3)
plt.plot(y , 'y' , y+1 , 'm ', y+2 ,'c')
plt.show()

#control the line style
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1,3)
plt.plot(y , '--' , y+1 , '-.', y+2 ,':')
plt.show()

#including markers

import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1,3,0.2)
plt.plot(y , 'x' , y+0.5 , 'o' , y+1 , 'D' , y+1.5 , '^' , y+2 , 's')
plt.show()

#histogram charts
import matplotlib.pyplot as plt
import numpy as np

y = np.random.randn(1000)
plt.hist(y)
plt.show()

#bar graph

import matplotlib.pyplot as plt

plt.bar([1,2,3] , [3,2,5])
plt.show()

#scattered plot
#bivarent analysis
x = np.random.randn(1000)
y = np.random.randn(1000)

plt.scatter(x , y)
plt.show()

#changing colour

size = 50*np.random.randn(1000)
colour = np.random.randn(1000)
plt.scatter(x , y , s = size , c = colour)
plt.show()

#Adding text inside graph

import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-4,4,1024)
Y = .25 * (X + 4.) * (X + 1.) * (X-2.)
plt.text(-0.5 , -0.25 , 'brachmard minimum')
plt.plot(X , Y , c = 'k')
plt.show()

#===============================seaborn module===============================

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
 """