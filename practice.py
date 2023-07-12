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
