import pandas as pd
from matplotlib import pyplot as plt
x = [1,2,3]
y = [1,4,9]
z=[10,5,0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("My first plot")
plt.xlabel("X")
plt.legend([1,2])
#sample_dataplt.show()
sample_data = pd.read_csv('sample_data.csv')
type(sample_data)
print(sample_data.column_c.iloc[0])
plt.plot(sample_data.column_a,sample_data.column_b)
plt.plot(sample_data.column_a,sample_data.column_c,'o')
plt.show()
data = pd.read_csv('countries.csv')
