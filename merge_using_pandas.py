import pandas as pd
import numpy as np


fh1 = open("file1.vcf", "r")
fh2 = open("file2.vcf","r")
writer = pd.ExcelWriter('output.xlsx')
df1 = pd.read_csv(fh1, sep ='\t', skiprows = 100)
df2 = pd.read_csv(fh2, sep ='\t', skiprows = 156)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
df1.to_excel(writer, index = False,sheet_name='CCP')
df2.to_excel(writer, index = False,sheet_name='OCAv3')
#print(data1)


#out = df1.merge(df2,left_on=('#CHROM','POS','REF','ALT'),right_on=('#CHROM','POS','REF','ALT'),how='inner',suffixes=('_CCP','__OCAv3')).head(10)
out = df1.merge(df2,left_on=('#CHROM','POS','REF','ALT'),right_on=('#CHROM','POS','REF','ALT'),how='inner',suffixes=('_CCP','__OCAv3'))

print(out)

out.to_excel(writer, index = False,sheet_name='common')
writer.save()










