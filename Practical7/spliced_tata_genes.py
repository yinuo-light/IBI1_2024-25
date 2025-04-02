# import the necessary library 
import re
# let user input the splice combination they look for
splice=input('Please enter the splice donor/acceptor combination in (GTAG,GCAG,ATAC):')
# Define a list of valid splice combinations
possibilities= ['GTAG', 'GCAG', 'ATAC']
# judge if the inputted splice combination is valid
if splice not in possibilities:
    print('Invalid splice combination. Please ensure you enter GTAG, GCAG, or ATAC')

# split the donor and acceptor in the splice combination   
donor=splice[0:2]
acceptor=splice[2:4]

# name the output file after the inputted splice combination 
output_file_path = f"{splice}_spliced_genes.fa"

# open the file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input_file, open(output_file_path, 'w') as output_file:
# set the viriables 
    name = None
    sequence = []
    
    for line in input_file:
# Remove whitespace at the beginning and end of a line 
        line = line.strip()  
# judge if the line is a line describe the information of the gene or a line of gene sequence
        if line.startswith('>'):  
            seq_str = ''.join(sequence)  
# use re.search to find if there are TATA boxs and donor and acceptor simultaneously in the gene            
            if re.search(r'TATA[AT]A[AT]', seq_str) and re.search(rf'{donor}.+{acceptor}',seq_str):  
#count the number of TATA box in the gene eligible                    
                    count=len(re.findall(r'TATA[AT]A[AT]', seq_str))  

# write the gene to the output file
# using regular expressions to get the gene's name
                    gene_name_match = re.search(r'gene:([^\s]+)', line)
                    name = gene_name_match.group(1)
                    output_file.write(f">{name} TATA_count:{count}\n{seq_str}\n")
                 
# after adding a gene with TATA box, reset the viriables for next gene        
            sequence = []
            name = None

# if the line is DNA sequence, append this line to the sequence  
        else:
            sequence.append(line)