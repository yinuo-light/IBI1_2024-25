#import the necessary library 
import re

#open the files
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input_file, open('tata_genes.fa', 'w') as output_file:
# set the viriables 
    name = None
    sequence = []
    
    for line in input_file:
# Remove whitespace at the beginning and end of a line 
        line = line.strip()  
# judge if the line is a line describe the information of the gene or a line of gene sequence
        if line.startswith('>'):  
            seq_str = ''.join(sequence)  
# use re.search to find if there are TATA boxs in the sequence            
            if re.search(r'TATA[AT]A[AT]', seq_str): 

# write the gene to the output file
# using regular expressions to get the gene's name
                    gene_name_match = re.search(r'gene:([^\s]+)', line)
                    name = gene_name_match.group(1)
                    output_file.write(f">{name}\n{seq_str}\n")
                
# after adding a gene with TATA box, reset the viriables for next gene
            sequence = []
            name = None

# if the line is DNA sequence, append this line to the sequence      
        else:
            sequence.append(line)