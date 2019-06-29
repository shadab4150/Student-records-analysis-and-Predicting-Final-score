import pandas as pd
from numpy import median
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D as axe

#plt.style.use('ggplot')

df=pd.read_csv('F:\\CSV files\\student_dataset.csv')

fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('workday alcohol consumption')
ax.set_zlabel('going out with friends')

ax.scatter(df.G3,df.Dalc,df.goout, c='red', marker='*')
plt.show()
plt.clf()

sns.set(style="darkgrid")
sns.pointplot(x='health',y='G3',hue="address",dodge=True,markers=["o","x"],linestyles=["-","--"],data=df)

plt.show()
plt.clf()

sns.set(style="darkgrid")
sns.lineplot(x='health',y='G3',hue='traveltime',data=df)
plt.show()
plt.clf()

sns.barplot(x='G3',y='health',data=df)
plt.show()
plt.clf()