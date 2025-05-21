# Define a function to determine the restriction enzyme cut	sites	
def cut(DNA, cut_sequence):  
   valid_nucleotides = {'A', 'C', 'G', 'T'}
# Check if the input sequence include wrong nucleotides  
   if not set(DNA).issubset(valid_nucleotides) or not set(cut_sequence). issubset(valid_nucleotides):
     raise ValueError("Contains invalid nucleotides. Only 'A', 'C', 'G', 'T' are allowed.")
# make a list to store cut site positions
   cut_sites = []   
# search in the DNA sequence for restriction enzyme cut	sites
   for i in range(len(DNA) - len(cut_sequence) + 1):
       if DNA[i:i + len(cut_sequence)] == cut_sequence:
# record the position of cut sites as i+1           
            cut_sites.append(i+1)
   return cut_sites

# an example of this function
try:
    DNA_sequence='ACGTCTACGTGCATGCGATCGACATGTGATTTCGAG'    
    Cut_sequence='CATG'
    result=cut(DNA_sequence,Cut_sequence)
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")    

# run the fuction
DNA_sequence=input("Please enter your DNA sequence:")
Cut_sequence=input("PLease enter your restriction enzyme cut site:")
result=cut(DNA_sequence,Cut_sequence)

# check if there exist a restriction enzyme cut sites
if result==[]:
  print("There is no restriction enzyme cut sites.")
else:
  print(result)