#merge two vcf

fc = open("file1.vcf","r")
lines = fc.readlines()

#print(olines)

v1chr =[]
v1pos = []
v1ref = []
v1alt =[]
v1rowlist = []
header = ""
for v1line in lines:
	if v1line.startswith("#"):
		header += v1line
	elif not v1line.startswith("#"):
		v1rowlist.append(v1line)
		v1line = v1line.split()
		v1pos.append(v1line[1])
		v1chr.append(v1line[0])
		v1ref.append(v1line[2])
		v1alt.append(v1line[3])
#print(v1rowlist)
#print(v1pos)
#print(v1alt)
fc.close()

fo = open("file2.vcf", "r")
olines = fo.readlines()
v2pos = []
v2chr =[]
v2ref =[]
v2alt =[]
v2rowlist = []
header2 = ""
for v2line in olines:
	if v2line.startswith("#"):
		header2 += v2line
	elif not v2line.startswith("#"):
		v2rowlist.append(v2line)
		v2line = v2line.split()
		v2pos.append(v2line[1])
		v2chr.append(v1line[0])
		v2ref.append(v1line[2])
		v2alt.append(v1line[3])
#print(v1rowlist)
#print(v2rowlist[0])
#print(v2pos)         #print POS column
#print (header2)

fout = open ("merged.vcf","w")
for i in range(len(v1pos)):
	for j in range(len(v2pos)):
		if ((v1pos[i]==v2pos[j]) & (v1ref[i]==v2ref[j]) & (v1alt[i]==v2alt[j])):
			#print (v1rowlist[i])
			fout.write(v1rowlist[i])
			

