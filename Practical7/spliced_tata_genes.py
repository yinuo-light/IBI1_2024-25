import re
input_file_path = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
splice=input('Please enter the sequence')
donor=splice[0:2]
acceptor=splice[2:4]

output_file_path = f"{splice}_spliced_genes.fa"

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    name = None
    sequence = []
    
    for line in input_file:
        line = line.strip()  # 去掉行首行尾的空白字符 
        if line.startswith('>'):  # 描述行
            seq_str = ''.join(sequence)  # 将多行序列合并为单行
            
            if re.search(r'TATA[AT]A[AT]', seq_str) and re.search(rf'{donor}.+{acceptor}',seq_str):  # 搜索 TATA 盒序列
                    
                    count=len(re.findall(r'TATA[AT]A[AT]', seq_str))  # 统计 TATA 盒的数量

                    gene_name_match = re.search(r'gene:([^\s]+)', line)
                    name = gene_name_match.group(1)# 获取第一个捕获组的内容
                    output_file.write(f">{name} TATA_count:{count}\n{seq_str}\n")
                
            # 重置序列
            sequence = []
            name = None
        else:
            # 累加序列
            sequence.append(line)