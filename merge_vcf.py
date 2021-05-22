#merge two vcf
import pandas as pd

fout = open("out.txt","w")
fc = open("file1.vcf","r")
data1 = fc.readlines()

#print(olines)
v1info =[]
v1chr =[]
v1pos = []
v1ref = []
v1alt =[]
v1rowlist = []
header = ""
for v1line in data1:
	if v1line.startswith("#"):
		header += v1line
	elif not v1line.startswith("#"):
		v1rowlist.append(v1line)
		v1line = v1line.split()
		v1pos.append(v1line[1])
		v1chr.append(v1line[0])
		v1ref.append(v1line[2])
		v1alt.append(v1line[3])
		v1info.append(v1line[7])
		
#print(v1rowlist)
#print(v1pos)
#print(v1alt)
#print(type(v1info))


#Stored info column data in pandas dataframe
df= pd.DataFrame(v1info)
df_ocav3 = pd.DataFrame(v2info)
#print(df)
split_data = df[0].str.split(";")
split_data_ocav3 = df_ocav3[0].str.split(";")
var = split_data.to_list()
var = split_data_ocav3.to_list()
new_df = pd.DataFrame(var, columns=None)
new_df_ocav3 = pd.DataFrame(var, columns=None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#print(new_df)
writer = pd.ExcelWriter('output.xlsx')
new_df.to_excel(writer, index = False,sheet_name='')
new_df_ocav3.to_excel(writer, index = False,sheet_name='')
writer.save()



fo = open("file2.vcf", "r")
data2 = fo.readlines()
v2info =[]
v2pos = []
v2chr =[]
v2ref =[]
v2alt =[]
v2rowlist = []
header2 = ""
for v2line in data2:
	if v2line.startswith("#"):
		header2 += v2line
	elif not v2line.startswith("#"):
		v2rowlist.append(v2line)
		v2line = v2line.split()
		v2pos.append(v2line[1])
		v2chr.append(v2line[0])
		v2ref.append(v2line[2])
		v2alt.append(v2line[3])
		v2info.append(v2line[7])
#print(v1rowlist)
#print(v2rowlist[0])
#print(v2pos)         #print POS column
#print (header2)
#print(v2info[0])
xlist =[]
fout = open ("merged.vcf","w")


for i in range(len(v1pos)):
	for j in range(len(v2pos)):
		if ((v1pos[i]==v2pos[j]) & (v1ref[i]==v2ref[j]) & (v1alt[i]==v2alt[j])):
			common_var = v1rowlist[i]     #common variants
			#x = common_var.split("\t")
			
			for element in v1info:
				element= element.split(";")
			
			#print(element)
			for element2 in v2info:
				element2 = element2.split(";")
			#print(element2[11])
"""	
for k in range(len(v1info)):   
	for j in range(len(v2info)):
			
"""	
			



	

		



		
