
fh1 = open("file1.vcf", "r")
data1 = fh1.readlines()
fh2 = open("file2.vcf","r")
data2 = fh2.readlines()
fout = open("result.xlsx", "w")
data3 = data2


header1 = ""
header2 = ""
uniqueccp = ""
merge = ""

for line1 in data1:
	counter =0
	if line1.startswith("#"):
		header1+=line1
	else:
		var1line = line1.split("\t")
		for line2 in data2:
			count = count + 1
			if line2.startswith ("#"):
				header2+=line2
			else:
				
				var2line = line2.split("\t")
				if ((var1line[0]==var2line[0]) and (var1line[1]==var2line[1]) and (var1line[3]==var2line[3]) and (var1line[4]==var1line[4])):
					counter+=1
					x = data3[count] == 0
					
	if (counter > 0):
		#merge += var1line[0]+"\t"+ var1line[1]+"\t"+var1line[2]+"\t"+var1line[3]+"\t"+var1line[4]+"\t"+var1line[5]+"\t"+var1line[6]+"\t"+var1line[7]+"\t"+var2line[7]
		merge += var1line[1] +"\t"
		
					#print(merge)
	else:
		uniqueccp += line1
merged = merge + uniqueccp
#print (type(merge))

#fout.write(str(merge))
print(uniqueccp)
#fout.write(merge)
						
					
			


