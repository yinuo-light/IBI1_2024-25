#import the necessary library 
import re

#enter the sequence
seq ='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
# use regular expression to greedy match the longest intron
seq1= re.findall(r'GT.+AG',seq)
# calculate the length and add it to the 'intron_lengths' list
intron_lengths = [len(intron) for intron in seq1]

# print out the result
print(seq1)
print(intron_lengths)
