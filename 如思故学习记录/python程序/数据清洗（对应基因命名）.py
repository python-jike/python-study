import re
with open(r'C:\Users\SEVEN\Desktop\fanqieceshi.fasta')as pro_file: # 输入你的总序列库(fasta、fas、fa)
    pro_list=pro_file.read().split(">")                 # 按行读取序列以>分隔并返回列表
with open(r'C:\Users\SEVEN\Desktop\1.txt') as pro_txt:  # 输入你的基因号文件（格式基因id 基因命名）
    gene = pro_txt.readlines()                   # 按行读取序列返回列表
fasta_dict={}
seq_out=[]
for id in gene:
    if id:
        id_out = id.split("\t")  # 按制表符分隔
        fasta_dict[id_out[0]] = id_out[1]  # 创建一个字典，key 基因id，value 基因命名
print(fasta_dict)
for key in fasta_dict.keys():
    '''
    根据特定基因命名，重新给蛋白文件的ID命名
    '''
    for seq in pro_list:
            if seq:
                seq_name = seq.split("\n")[0]  # 提取基因ID
                seq_fa = "".join(seq.split("\n")[1:])  # 提取出序列
                reg = re.compile('{}'.format(key))  # 匹配模式基因id
                result = reg.findall(seq_name)
                # print(seq_fa)
                if result:
                    seq_out.append(">" + fasta_dict[key].strip() + "\n" + seq_fa + "\n")
                    pass
                pass
print(seq_out)
with open(r'C:\Users\SEVEN\Desktop\ceshi.fasta','w',encoding='UTF-8') as f1:
    for name in seq_out:
        '''
        输出数据清洗后的fasta文件到ceshi.fasta文件中
        '''
        if name:
            f1.write(name)
