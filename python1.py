import pandas as pd
import openpyxl
#def ProcedureCode1, HCPCCode1, CPTModifier1,ServiceLineCharge1,UnitQty1,ServiceFromDate1,ServiceToDate1 as str
#excel_file="C:\Users\supriya\Desktop\data.xlsx"
df=pd.read_excel("C:/Users/supriya/Desktop/data.xlsx")
print(df)
#value=df.loc['JOHN']
print(df[df.columns[0:4]])  
ProcedureCode1 = df[df.columns[37:38]]
print(ProcedureCode1)
HCPCCode1 = df[df.columns[38:39]]
print(HCPCCode1)
#             Trim(Worksheets("Testdata").Range("AL" & i).Value)
#             HCPCCode1 = Trim(Worksheets("Testdata").Range("AM" & i).Value)
#             CPTModifier1 = Trim(Worksheets("Testdata").Range("AN" & i).Value)
#             ServiceLineCharge1 = Trim(Worksheets("Testdata").Range("AO" & i).Value)
#             UnitQty1 = Trim(Worksheets("Testdata").Range("AP" & i).Value)
#             ServiceFromDate1 = Trim(Worksheets("Testdata").Range("AQ" & i).Value)
#             ServiceToDate1 = Trim(Worksheets("Testdata").Range("AR" & i).Value)
cd de