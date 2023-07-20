'''
GitHub pass->
mohdshayyan1@gmail.com
shayyanpathan830
'''
import pandas as pd

#--------------------------------------------------------- Series -------------------------------------------------------------------

#x=pd.Series([10,20,30],index=['kam','Jam','tam'])#(['kam','Jam','tam'],index=[10,20,30])     #,dtype=np.object_)
# tam ko 35 pr:-->
#x['tam']=35
# Modify full index in series:-->
#x.index=['k','J','t']
#print(x)
# Slicing:-->
#x=x[x>10]
#print(x)
'''
df[20]=25
df=df.T
df=df.drop(10,axis=0)
df[25]='Jam'
print(df)
'''
#Naming index:-->
#x.index.name='Name'
#x.name='Result'
#print(x)

#--------------------------------------------------------- DataFrame -------------------------------------------------------------------

'''idx=['Sub1','Sub2','Sub3']
data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
df=pd.DataFrame(data,index=idx)'''
# Add a Column in df:-->
#df['D']=[10,11,12]
# Add a Row in df:-->
#df.loc['Sub4']=[10,11,12]

# Drop a Column in df:-->
#df=df.drop(['C'],axis=1)
# Drop a Row in df:-->
#df=df.drop(['Sub3'],axis=0)

# Rename a Column in df:-->
#df=df.rename({'A':'A1'},axis='columns')
# Rename a Row(Index) in df:-->
#df=df.rename({'Sub3':'S3'})#,axis='index')

###print(df)

#----------------------------------
'''


data = {2014: [100.5, 150.8, 200.9, 30000, 40000],
        2015: [12000, 18000, 22000, 30000, 45000],
        2016: [20000, 50000, 70000, 100000, 125000],
        2017: [50000, 60000, 70000, 80000, 90000]}
index = ['Madhu', 'kusum', 'kinshuk', 'Ankit', 'Shuriti']
Sales = pd.DataFrame(data, index=index)

Sales2 = pd.DataFrame({2018: [50000]}, index=['Neha'])  # Corrected the dimensions of Sales2
Sales = Sales._append(Sales2)
print(Sales)
#b)
print(Sales.T)
#c)
print(Sales[2017])
#d)
selected_sales = Sales.loc[['Madhu', 'Ankit'], [2017, 2018]]  
print(selected_sales)
#e)
selected_sales = Sales.loc[['Shruti'], [2016]]  
print(selected_sales)

#(f)
salesman_data = [196.2, 37800, 52000, 78438, 38852]
years = [2014, 2015, 2016, 2017, 2018]
Sales.loc['Sumeet'] = salesman_data
print(Sales)

# g) delete the data for the year 2014 from DataFrame Sales.
# Delete data for the year 2014
Sales = Sales.drop(columns=[2014])

print(Sales)

# h) delete the data for salesman kinshuk from  the dataframe sales.
# Delete data for the salesman "kinshuk"
Sales = Sales.drop('kinshuk')
print(Sales)

# i) change the name of the salesperson Ankit to vivaan and Madhu to Shailesh.
# Change the names "Ankit" to "Vivaan" and "Madhu" to "Shailesh"
Sales = Sales.rename(index={'Ankit': 'Vivaan', 'Madhu': 'Shailesh'})
print(Sales)

# J) Update the sales made by Shailesh in 2018 to 100000.
# Update the sales made by "Shailesh" in 2018 to 100000
Sales.loc['Shailesh', 2018] = 100000
print(Sales)

# (K)write the values of dataframe Sales to a comma separated file salesFigures.csv on the disk. do not write the row lables and column lables.
# Write DataFrame values to a CSV file without row labels and column labels
Sales.to_csv('salesFigures.csv', header=False, index=False)
print("Sales data has been written to salesFigures.csv")

'''
