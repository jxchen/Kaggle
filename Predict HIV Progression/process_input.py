import pickle

NUM_AMINO_ACID_CATEGORIES = 21
MAX_PRSEQ_LENGTH = 99
MAX_RTSEQ_LENGTH = 494

cmap = pickle.load(open('cmap.pkl','rb'))
nmap = pickle.load(open('nmap.pkl','rb'))

def main():
	fin = open('test_data.csv','r')
	fin.readline()
	
	fout = open('processed_test_data.csv','w')
	fout_data = []
	
	for line in fin:
		splitLine = line.strip().split(',')
		temp_fout_data = []
		
		temp_fout_data.append(splitLine[1])
		
		converted_prseq = convert(splitLine[2])
		if len(splitLine[2])/3 < MAX_PRSEQ_LENGTH:
			converted_prseq += '1' * (NUM_AMINO_ACID_CATEGORIES * (MAX_PRSEQ_LENGTH - len(splitLine[2])/3))
		temp_fout_data.append(converted_prseq)
		
		converted_rtseq = convert(splitLine[3])
		if len(splitLine[3])/3 < MAX_RTSEQ_LENGTH:
			converted_rtseq += '0' * (NUM_AMINO_ACID_CATEGORIES * (MAX_RTSEQ_LENGTH - len(splitLine[3])/3))
		temp_fout_data.append(converted_rtseq)
		
		temp_fout_data.append(splitLine[4])
		temp_fout_data.append(splitLine[5])
		fout_data.append(temp_fout_data)
	
	#mean-normalize vload and CD4 count
	vloads = [float(x[3]) for x in fout_data]
	cd4counts = [float(x[4]) for x in fout_data]
	
	mean_vloads = mean(vloads)
	range_vloads = float(max(vloads)-min(vloads))
	mean_cd4counts = mean(cd4counts)
	range_cd4counts = float(max(cd4counts)-min(cd4counts))
	
	for i in range(len(fout_data)):
		fout_data[i][3] = str((float(fout_data[i][3]) - mean_vloads) / range_vloads)
		fout_data[i][4] = str((float(fout_data[i][4]) - mean_cd4counts) / range_cd4counts)
	
	#insert commas inside amino acid category data to turn it into a matlab-acceptable matrix
	for i in range(len(fout_data)):
		fout_data[i][1] = insertCommas(fout_data[i][1])
		fout_data[i][2] = insertCommas(fout_data[i][2])
	
	fout.write('\n'.join([','.join(item) for item in fout_data]))
	
	fin.close()
	fout.close()

#inserts comma separators into the string
def insertCommas(string):
	temp = []
	for char in string:
		temp.append(char)
		temp.append(',')
	return ''.join(temp[:-1])

#returns binary amino acid sequence from raw nucleotide coding string
def convert(nucleotides):
	out_arr = []
	
	#cut off any trailing nucleotides
	remainder = len(nucleotides)%3
	if remainder > 0:
		nucleotides = nucleotides[:-remainder]
	
	for i in range(0,len(nucleotides),3):
		out_arr.append(possible_amino_acids(nucleotides[i:i+3]))
	return ''.join(map(str,[item for sublist in out_arr for item in sublist]))

#returns a categorical array of possible amino acids given a 3-sequence codon
def possible_amino_acids(codon):
	categories = [0]*NUM_AMINO_ACID_CATEGORIES
	c0 = nmap[codon[0]]
	c1 = nmap[codon[1]]
	c2 = nmap[codon[2]]		
	
	for x in c0:
		for y in c1:
			for z in c2:
				categories[cmap[x+y+z]] = 1
	return categories

def mean(lst):
	return 1.0*sum(lst)/len(lst)
	
if __name__ == '__main__':
	main()
