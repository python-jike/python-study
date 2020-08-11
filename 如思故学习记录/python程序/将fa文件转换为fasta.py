with open(r"C:\Users\SEVEN\Desktop\osa.fa") as seq_file:             # 输入你的总序列库(fasta、fas、fa)
    seq_list=seq_file.read().split(">")                             # 将序列以>号分隔开
seq_list1=[]
for seq in seq_list:
    '''
    删除序列间的换行符，输出序列
    '''
    if seq:
        seq_name = seq.split("\n")[0]                           # 提取基因ID
        seq_fa = "".join(seq.split("\n")[1:])                   # 提取出序列
        seq_list1.append(">" + seq_name + "\n" + seq_fa + "\n") # 拼接基因ID和基因序列
# print(seq_list1) 检验是否成功拼接，检验用，慎用
with open(r'C:\Users\SEVEN\Desktop\test1.fasta', 'w', encoding='UTF-8') as f1:
    for xulie in seq_list1:
        '''
        将整理好的序列重新写入新的test1.fasta文件中
        '''
        if xulie:
            f1.write(xulie)
