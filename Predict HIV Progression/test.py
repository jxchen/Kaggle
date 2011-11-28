f = open('test_data.csv','r')

f.readline()

max1 = 0
max2 = 0

for line in f:
	splitLine = line.strip().split(',')
	max1 = max(max1,len(splitLine[2]))
	max2 = max(max2,len(splitLine[3]))
	
print max1
print max2
