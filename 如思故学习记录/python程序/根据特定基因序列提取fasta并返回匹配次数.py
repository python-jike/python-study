import re
with open(r"C:\Users\SEVEN\Desktop\osa.fa") as seq_file: # 输入你的总序列库(fasta、fas、fa)
    seq_list=seq_file.read().split(">")              # 将序列以>号分隔开
seq_list1=[]
seq_list2=[]
for seq in seq_list:
    '''
    根据特定基因序列，提取存在该序列的fasta文件，并返回序列的匹配次数
    '''
    if seq:
        seq_name = seq.split("\n")[0]            # 提取基因ID
        seq_fa = "".join(seq.split("\n")[1:])    # 提取出序列
        reg = re.compile('TTAGGG')              # 要匹配的特定基因序列
        result = reg.findall(seq_fa,re.I)       # 要匹配的特定基因序列(忽略大小写)
        if result:
            seq_num = str(len(result))
            seq_list1.append(">" + seq_name + "\t"+'(' + seq_num + ')' + "\n") # 导出对应的基因ID以及匹配次数
            seq_list2.append(">" + seq_name + "\n" + seq_fa + "\n")            # 拼接基因ID和基因序列
print(seq_list1)                                 # 输出seq_list1以查看是否匹配到
'''
将筛选出的基因ID和匹配次数以txt格式输出到test1文件中去
'''
with open(r'C:\Users\SEVEN\Desktop\test3.txt', 'w', encoding='UTF-8') as f1: 
    for name in seq_list1:
        if name:
            f1.write(name)
'''
将根据特定基因序列筛选出的基因序列以fasta格式输出到test4文件中去
'''
with open(r'C:\Users\SEVEN\Desktop\test4.fasta','w',encoding='UTF-8') as f2:
    for xulie in seq_list2:
        if xulie:
            f2.write(xulie)


