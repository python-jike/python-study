import re
with open(r"C:\Users\SEVEN\Desktop\ath.gff")as gff_file: # 输入你的总序列库(fasta、fas、fa)
    gff_list=gff_file.readlines()                # 按行读取序列返回列表
with open(r"C:\Users\SEVEN\Desktop\1.txt") as gff_txt:  # 输入你的基因号文件
    gene = gff_txt.readlines()                   # 按行读取序列返回列表
bed_dict={}
for id in gene:
    if id:
        id_out = id.split("\t")  # 按制表符分隔
        bed_dict[id_out[0]] = id_out[1]  # 创建一个字典，key 基因id，value 基因命名
print(bed_dict)
gff_list1=[]
start1 = 0
for key in bed_dict.keys():
    '''
    根据特定基因id，提取基因注释文件，转化为适合GSDS分析的BED格式
    '''
    for line in gff_list:
        if line:
            gff_out = line.strip().split("\t")  # 按制表符分隔每行注释
            gff_id = gff_out[-1]    # 提取出id
            reg = re.compile('{}'.format(key))  # 匹配模式【基因id】
            result = reg.findall(gff_id)        # 返回所有的匹配结果
            if result:
                if gff_out[2] =='mRNA':
                    gff_out[2] = 'gene'
                    start1 =int(gff_out[3])
                start = int(gff_out[3]) - start1
                end = int(gff_out[4]) - start1
                # two=str(gff_out[2])
                # seven = str(gff_out[7])
                gff_list1.append(str(bed_dict[key]).strip()+'\t'+str(start)+'\t'+str(end)+'\t'+gff_out[2]+'\t'+'\t'+gff_out[7]+'\n')
                pass
            pass
with open(r'C:\Users\SEVEN\Desktop\bed1.txt','w',encoding='UTF-8') as f1:
    for seq in gff_list1:
        '''
        输出BED格式的文件到bed.txt文件中
        '''
        if seq:
            f1.write(seq)
with open(r'C:\Users\SEVEN\Desktop\bed2.txt','w',encoding='UTF-8') as f2:
    for seq in gff_list1:
        '''
        输出BED格式的文件到bed.txt文件中（选出特定的位置，cds、gene）
        '''
        if seq:
            # print(seq)
            seq_out = seq.strip().split("\t")  # 提取基因ID
            # seq_out1 = seq_out.remove('')
            # print(seq_out)
            seq_id = seq_out[3]  # 提取出序列
            reg = re.compile('CDS|gene')
            result1 = reg.findall(seq_id)
            if result1:
                f2.write(seq)

