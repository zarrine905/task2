#merge two vcf

fc = open("file1.vcf","r")
lines = fc.readlines()

#print(olines)

v1pos = []
v1rowlist = []
header = ""
for v1line in lines:
	if v1line.startswith("#"):
		header += v1line
	elif not v1line.startswith("#"):
		v1rowlist.append(v1line)
		v1line = v1line.split()
		v1pos.append(v1line[1])
		
#print(v1rowlist)
#print(v1pos)
fc.close()

fo = open("file2.vcf", "r")
olines = fo.readlines()
v2pos = []
v2rowlist = []
header2 = ""
for v2line in olines:
	if v2line.startswith("#"):
		header2 += v2line
	elif not v2line.startswith("#"):
		v2rowlist.append(v2line)
		v2line = v2line.split()
		v2pos.append(v2line[1])
print(v2rowlist[0])
#print(v2pos)         #print POS column
#print (header2)

