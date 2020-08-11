with open(r"C:\Users\SEVEN\Desktop\cafei.blast") as blast_file:  # 输入你的blast比对文件
    blast_list=blast_file.readlines()                       # 读取文件，按行作为列表返回
seq_list1=[]
for seq_id in blast_list:
    '''
    根据特定基因序列，提取存在该序列的fasta文件，并返回序列的匹配次数
    '''
    if seq_id:
        blast_out = seq_id.split("\t")  # 以制表符分隔blast结果
        blast_score= int(blast_out[3])  # 提取得分值
        if  blast_score > 100:
            seq_list1.append(seq_id)
print(seq_list1)

'''
将根据特定条件筛选出的基因序列ID输出到test4文件中去
'''
with open(r'C:\Users\SEVEN\Desktop\test4.txt','w',encoding='UTF-8') as f1:
    for jieguo in seq_list1:
        if jieguo:
            f1.write(jieguo)