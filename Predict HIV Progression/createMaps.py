import pickle

cmap = {}

#keys = DNA codons, values = indices of amino acid in array

"""amino acid array:
A
C
D
E
F
G
H
I
K
L
M
N
P
Q
R
S
T
V
W
Y
STOP"""

cmap['GCT'] = 0
cmap['GCC'] = 0
cmap['GCA'] = 0
cmap['GCG'] = 0

cmap['TGT'] = 1
cmap['TGC'] = 1

cmap['GAT'] = 2
cmap['GAC'] = 2

cmap['GAA'] = 3
cmap['GAG'] = 3

cmap['TTT'] = 4
cmap['TTC'] = 4

cmap['GGT'] = 5
cmap['GGC'] = 5
cmap['GGA'] = 5
cmap['GGG'] = 5

cmap['CAT'] = 6
cmap['CAC'] = 6

cmap['ATT'] = 7
cmap['ATC'] = 7
cmap['ATA'] = 7

cmap['AAA'] = 8
cmap['AAG'] = 8

cmap['TTA'] = 9
cmap['TTG'] = 9
cmap['CTT'] = 9
cmap['CTC'] = 9
cmap['CTA'] = 9
cmap['CTG'] = 9

cmap['ATG'] = 10

cmap['AAT'] = 11
cmap['AAC'] = 11

cmap['CCT'] = 12
cmap['CCC'] = 12
cmap['CCA'] = 12
cmap['CCG'] = 12

cmap['CAA'] = 13
cmap['CAG'] = 13

cmap['CGT'] = 14
cmap['CGC'] = 14
cmap['CGA'] = 14
cmap['CGG'] = 14
cmap['AGA'] = 14
cmap['AGG'] = 14

cmap['TCT'] = 15
cmap['TCC'] = 15
cmap['TCA'] = 15
cmap['TCG'] = 15
cmap['AGT'] = 15
cmap['AGC'] = 15

cmap['ACT'] = 16
cmap['ACC'] = 16
cmap['ACA'] = 16
cmap['ACG'] = 16

cmap['GTT'] = 17
cmap['GTC'] = 17
cmap['GTA'] = 17
cmap['GTG'] = 17

cmap['TGG'] = 18

cmap['TAT'] = 19
cmap['TAC'] = 19

cmap['TAA'] = 20
cmap['TGA'] = 20
cmap['TAG'] = 20

pickle.dump(cmap,open('cmap.pkl','wb'))

nmap = {}

nmap['A'] = 'A'
nmap['C'] = 'C'
nmap['G'] = 'G'
nmap['T'] = 'T'

nmap['R'] = 'AG'
nmap['Y'] = 'CT'
nmap['M'] = 'AC'
nmap['K'] = 'GT'
nmap['W'] = 'AT'
nmap['S'] = 'CG'
nmap['B'] = 'CTG'
nmap['D'] = 'ATG'
nmap['H'] = 'ACT'
nmap['V'] = 'ACG'
nmap['N'] = 'ACGT'

pickle.dump(nmap,open('nmap.pkl','wb'))
