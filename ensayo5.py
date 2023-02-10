import pandas as pd 
import openpyxl


df=pd.DataFrame


df1=pd.read_excel("raw_scrap28.xlsx", engine="openpyxl")
df2=pd.read_excel("raw_scrap20.xlsx",engine="openpyxl")

# merge "outer" devuelve  union de df1 y df2 sin duplicado

df3= pd.merge(left=df1["URL"],right=df2["URL"],how="outer")
print (df3)




#df3= pd.merge(left=df1["URL"],right=df2["URL"],how="left")
#df3. to_excel("resultado2.xlsx")


#df3=pd.read_excel("resultado2.xlsx",engine="openpyxl")

#df4= pd.merge(df3["URL"],df1["URL"],how="inner")
#df4. to_excel("resultado4.xlsx")

#df4= pd.merge(df3["URL"],df2["URL"],how="inner")
#df4. to_excel("resultado3.xlsx")

#df3= pd.merge(left=df1["URL"],right=df2["URL"],how="left")
#df3. to_excel("resultado2.xlsx")

#df3= pd.merge(df1["URL"],df2["URL"],how="inner").head(100)
#df3. to_excel("resultado.xlsx")














