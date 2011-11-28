from __future__ import division
import sys

NUM_INPUT_FEATURES = 10

f1 = open('cs-training.csv','r')
f2 = open('cs-test.csv','r')

f1.readline()
f2.readline()

mean_arr = [0] * NUM_INPUT_FEATURES
max_arr = [-sys.maxint-1] * NUM_INPUT_FEATURES
min_arr = [sys.maxint] * NUM_INPUT_FEATURES
count_arr = [0] * NUM_INPUT_FEATURES

for line in f1:
	splitLine = line.strip().split(',')[2:]
	if len(splitLine) > 1:
		for i in range(NUM_INPUT_FEATURES):
			if splitLine[i] != 'NA':
				mean_arr[i] += float(splitLine[i])
				max_arr[i] = max(max_arr[i],float(splitLine[i]))
				min_arr[i] = min(min_arr[i],float(splitLine[i]))
				count_arr[i] += 1
for line in f2:
	splitLine = line.strip().split(',')[2:]
	if len(splitLine) > 1:
		for i in range(NUM_INPUT_FEATURES):
			if splitLine[i] != 'NA':
				mean_arr[i] += float(splitLine[i])
				max_arr[i] = max(max_arr[i],float(splitLine[i]))
				min_arr[i] = min(min_arr[i],float(splitLine[i]))
				count_arr[i] += 1

mean_arr = [mean_arr[i] / count_arr[i] for i in range(NUM_INPUT_FEATURES)]

f1.close()
f2.close()

#scale inputs and save to csv
f1 = open('cs-training.csv','r')
f2 = open('cs-test.csv','r')
fwrite = open('scaled-cs-both.csv','w')

f1.readline()
f2.readline()

for line in f1:
	splitLine = line.strip().split(',')
	if len(splitLine) > 1:
		for i in range(NUM_INPUT_FEATURES):
			if splitLine[i+2] != 'NA':
				splitLine[i+2] = '%.4f' % ((float(splitLine[i+2]) - mean_arr[i]) / (max_arr[i] - min_arr[i]))
			else:
				splitLine[i+2] = '0'
		fwrite.write(','.join(splitLine[1:]) + '\n')
for line in f2:
	splitLine = line.strip().split(',')
	if len(splitLine) > 1:
		for i in range(NUM_INPUT_FEATURES):
			if splitLine[i+2] != 'NA':
				splitLine[i+2] = '%.4f' % ((float(splitLine[i+2]) - mean_arr[i]) / (max_arr[i] - min_arr[i]))
			else:
				splitLine[i+2] = '0'
		fwrite.write('-1,' + ','.join(splitLine[2:]) + '\n')

f1.close()
f2.close()
fwrite.close()
	
