import re
import operator

def NucleotideCounter(DNA):
        result = [0, 0, 0, 0]
        for base in DNA:
                if base == "A":
                        result[0] += 1
                elif base == "C":
                        result[1] += 1
                elif base == "G":
                        result[2] += 1
                elif base == "T":
                        result[3] += 1
        result = " ".join(map(str, result))
        return result
        #consider using dictionary so you loop once and without if/elses. or simply use the count function (possibly with map or generator expresssion)

def RnaTranscriber(DNA):
	mrna = ""
	for base in DNA:
		if base == "T":
			mrna += "U"
		else:
			mrna += base
	return mrna
#consider using string replace

def ReverseComp(DNA):
	comp = ""
	for base in reversed(DNA):
		if base == "A":
			comp += "T"
		elif base == "T":
			comp += "A"
		elif base == "C":
			comp += "G"
		elif base == "G":
			comp += "C"
	return comp
#replace with lower letters and then upper. 
#maketrans function
#dictionary {A:T etc} or automatic with dict(zip("ACGT", "TGCA"))

def RabbitFibo(months, babies=1):
	a, b = 1, 1
	for i in range(months-1):
		a, b = b, babies*a + b
	return a
#memoize/recursive this in order to make it faster. dynamic programming: build up from n=1 case

def HighGC(DNA_file):
	DNA = DNA_file.replace('\n', ' ').replace('\r', ' ')
	regex = r"(>Rosalind_\d{4}) ([ACGT\s]*)"
	matchList = re.findall(regex, DNA)
	DNAdict = {}
	result = ''
	for case in matchList:
		DNAdict[case[0].replace('>', '')] = [case[1].replace(' ', '')]
	for gene in DNAdict:
		curr_gene = DNAdict[gene][0]
		gc_count = GC_Count(curr_gene)
		gc_per = gc_count*100/len(curr_gene)
		DNAdict[gene].append(gc_per)
	maxval = max(DNAdict.values(), key=operator.itemgetter(1))
	for key, value in DNAdict.items():
		if value[1] == maxval[1]:
			result += '{} {}'.format(key, value[1])
	return result
#try to reduce for loops. convert things into while true loops. with that, proceed through fasta file line by line. Each line check for > and append that line to DNAdict or fastaid_list. Then proceed to next line and as long as its not empty or startswith(>) then append to DNAdict[label] or to seq_list
#can avoid use of regex and operator. simply use string.startswith(), string.rstrip(), file.readline, and file.split() .

def GC_Count(DNA):
	gc_count = 0
	for base in DNA:
		if base == "C" or base == "G":
			gc_count += 1
	return gc_count
#convert gc if loop into just str.count(g)
