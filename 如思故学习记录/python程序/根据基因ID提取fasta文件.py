import re
with open(r"C:\Users\SEVEN\Desktop\ath.fasta") as seq_file: # 输入你的总序列库(fasta、fas、fa)
    seq_list=seq_file.read().split(">")                 # 将序列以>号分隔开
with open(r"C:\Users\SEVEN\Desktop\1.txt") as seq_txt:    # 输入你的基因号文件
    seq_id = seq_txt.read().split('\n')                  # 将基因ID以\n分隔开
seq_out=[]
for id in seq_id:
    '''
    根据特定基因ID，提取fasta文件
    '''
    for seq in seq_list:
        if seq:
            seq_name = seq.split("\n")[0]  # 提取基因ID
            seq_fa = "".join(seq.split("\n")[1:])  # 提取出序列
            reg = re.compile('{}'.format(id)) #匹配模式基因id
            result = reg.findall(seq_name)
            if result:
                seq_out.append(">" + seq_name + "\n" + seq_fa+ "\n") # 拼接成fasta格式

print(seq_out)                                      # 输出提取出来的基因或的蛋白序列
'''
将根据基因ID筛选出的基因序列输出到test1文件中去
'''
with open(r'C:\Users\SEVEN\Desktop\test1.fasta','w',encoding='UTF-8') as f1:
    for xulie in seq_out:
        if xulie:
            f1.write(xulie)