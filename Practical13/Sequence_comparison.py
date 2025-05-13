# create an empty dictionary to store the BLOSUM62 matrix
blosum62 = {}
# Open the BLOSUM.txt file in read mode
with open('BLOSUM.txt','r') as file:
        lines = file.readlines()
# Extract the amino acids from the first line of the file
amino_acids = lines[0].strip().split()
# Split the line into scores, ignoring amino acid symbols
for i, line in enumerate(lines[1:]):
        scores = line.strip().split()[1:]
        for j, score in enumerate(scores):
            blosum62[(amino_acids[i], amino_acids[j])] = int(score)


# create a function to read the fasta file
def read_fasta(file_path):
    # open the file and read all lines    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    #Remove any leading or trailing whitespace
    #Append the stripped line to the sequence string
    sequence = ''.join(line.strip() for line in lines[1:])
    return sequence


# create a function to calculate the alighment score
def calculate_alignment_score(seq1, seq2, blosum62):
    # initialize score and count number
    score = 0
    identical_count = 0
    for i in range(len(seq1)):
        # ADD the score from blosum62 for (seq1[i], seq2[i]) to score
        score += blosum62[(seq1[i], seq2[i])]
        if seq1[i] == seq2[i]:
            # count the number of the same amino acids 
            identical_count += 1
    return score, identical_count / len(seq1) * 100

# use a main function to combine all the function implementations for the calculation
def main():
    seq1 = read_fasta('P04179.fasta')
    seq2 = read_fasta('P09671.fasta')
    seq_random = read_fasta('random.fasta')

    score1, identity1 = calculate_alignment_score(seq1, seq2, blosum62)
    score2, identity2 = calculate_alignment_score(seq1, seq_random, blosum62)
    score3, identity3 = calculate_alignment_score(seq2, seq_random, blosum62)
    
    print(f"Human vs Mouse: Score = {score1}, Identity = {identity1:.2f}%")
    print(f"Human vs Random: Score = {score2}, Identity = {identity2:.2f}%")
    print(f"Mouse vs Random: Score = {score3}, Identity = {identity3:.2f}%")

if __name__ == "__main__":
    main()