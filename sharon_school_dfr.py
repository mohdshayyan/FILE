import pandas as pd

data={'A':[67,89,90,95],'B':[20,50,60,94],'C':[70,80,90,60],'D':[80,90,59,85]}
idx=['Physics','Biology','English','Chemistry']
df=pd.DataFrame(data,index=idx)
#-------------------------------------------------------------------------
# Adding a col to dataFrame
#df['E']=[80,90,70,60]
# OR
# Adding same values a col to dataFrame
#df['E']=99
#-------------------------------------------------------------------------
# Adding a Row to DataFrame
#df.loc['IP']=[80,90,70,60]
# OR
#df.loc['IP']=99
#-------------------------------------------------------------------------
#Set all the Values to zero
#df[:]=0
#-------------------------------------------------------------------------
# To Drop a Row From DataFrame:
#df=df.drop('English',axis=0) #It is used to drop duplicate Row also:
# OR
# To Drop a col. From DataFrame:
#df=df.drop('D',axis=1)
#-------------------------------------------------------------------------
# To Rename Index(Rows)->
#df=df.rename({'Physics':'Phy'}) #,axis='index')
# To Rename Columns->
#df=df.rename({'A': 'a1'},axis='columns')
#-------------------------------------------------------------------------
# Label Based indexing->
#df=df.loc['Biology']
# Boolean Based indexing->
#df=df.loc['Biology']>10
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Print the DataFrame
print(df)
#df.to_csv('Pd')
