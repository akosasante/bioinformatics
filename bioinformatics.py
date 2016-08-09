def PatternCount(Pattern, Text):
    count = 0
    window = len(Text) - len(Pattern)
    for i in range(window+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count


def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates 

def remove_duplicates(x_list):
    new_list = []
    for x in x_list:
        if x not in new_list:
            new_list.append(x)
    return new_list

def reverse(text):
    new_text = ""
    for letter in text:
        new_text = letter + new_text
    return new_text

def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    compDict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    comp += compDict[Nucleotide] 
    return comp

def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    revPattern = reverse(Pattern)
    for base in revPattern:
        compBase = complement(base)
        revComp += compBase
    return revComp

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

def Skew(Genome):
    skew = {}
    n = len(Genome)+1
    skew[0] = 0
    for i in range(1, n):
        if Genome[i-1] == "G":
            skew[i] = skew[i-1] + 1
        elif Genome[i-1] == "C":
            skew[i] = skew[i-1] - 1
        else:
            skew[i] = skew[i-1]
    return skew

def MinSkew(Genome):
    min_skew = []
    skew = Skew(Genome)
    min_value = min(skew.values())
    for key, value in skew.items():
        if value == min_value:
            min_skew.append(key)
    return min_skew

def HammingDistance(p, q):
    distance = 0
    for i, base in enumerate(p):
        if base != q[i]:
            distance += 1
    return distance

def ApproximatePatternMatching(Pattern, Text, d):
    positions = []
    window = len(Text) - len(Pattern)
    for i in range(window+1):
        current_pattern = Text[i:i+len(Pattern)]
        if HammingDistance(current_pattern, Pattern) <= d:
            positions.append(i)
    return positions

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    window = len(Text) - len(Pattern)
    for i in range(window+1):
        current_pattern = Text[i:i+len(Pattern)]
        if HammingDistance(current_pattern, Pattern) <= d:
            count += 1
    return count

    
oriC_vibrio = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

oriC_thermo = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"
