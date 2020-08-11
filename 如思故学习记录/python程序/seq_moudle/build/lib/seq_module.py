import re
def blast(in1,out1):
    '''
    提取blast文件中得分值大于100的基因id
    :param in1: 输入你的blast比对文件(文件目录)
    :param out1: 将根据特定条件筛选出的基因序列ID输出到out文件中去(文件目录)
    :return:NONE
    '''
    with open(in1) as blast_file:  # 输入你的blast比对文件
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
    with open(out1,'w',encoding='UTF-8') as f1:
        for jieguo in seq_list1:
            if jieguo:
                f1.write(jieguo)
if __name__ =='main':
    in1=r"C:\Users\SEVEN\Desktop\cafei.blast"
    out1=r'C:\Users\SEVEN\Desktop\test4.txt'
    blast(in1,out1)
    print('测试1')
def fa(in1,out1):
    '''
    将fa格式文件转化为fasta格式文件，删除序列间的换行符，输出序列
    :param in1: # 输入你的总序列库(fasta、fas、fa)（文件目录）
    :param out1:将整理好的序列重新写入新的目的文件中，fasta格式（文件目录）
    :return:
    '''
    with open(in1) as seq_file:             # 输入你的总序列库(fasta、fas、fa)
        seq_list=seq_file.read().split(">")                             # 将序列以>号分隔开
    seq_list1 = []
    for seq in seq_list:
        '''
        删除序列间的换行符，输出序列
        '''
        if seq:
            seq_name = seq.split("\n")[0]                           # 提取基因ID
            seq_fa = "".join(seq.split("\n")[1:])                   # 提取出序列
            seq_list1.append(">" + seq_name + "\n" + seq_fa + "\n") # 拼接基因ID和基因序列
    # print(seq_list1) 检验是否成功拼接，检验用，慎用
    with open(out1, 'w', encoding='UTF-8') as f1:
        for xulie in seq_list1:
            '''
            将整理好的序列重新写入新的test1.fasta文件中
            '''
            if xulie:
                f1.write(xulie)
if __name__ =='main':
    in1=r"C:\Users\SEVEN\Desktop\osa.fa"
    out1=r'C:\Users\SEVEN\Desktop\test1.fasta'
    fa(in1,out1)    
    print('测试2')
def fasta(in1,in2,out1):
    '''
    根据特定基因ID，提取fasta文件
    :param in1: 输入你的总序列库(fasta、fas、fa)（文件目录）
    :param in2: 输入你的基因号文件(换行符分隔)（文件目录）
    :param out1: 将根据基因ID筛选出的基因序列输出到目的文件中去（文件目录）
    :return:
    '''
    with open(in1) as seq_file: # 输入你的总序列库(fasta、fas、fa)
        seq_list=seq_file.read().split(">")                 # 将序列以>号分隔开
    with open(in2) as seq_txt:    # 输入你的基因号文件
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
    with open(out1,'w',encoding='UTF-8') as f1:
        for xulie in seq_out:
            if xulie:
                f1.write(xulie)
if __name__ =='main':
    in1=r"C:\Users\SEVEN\Desktop\ath.fasta"
    in2=r"C:\Users\SEVEN\Desktop\1.txt"
    out1=r'C:\Users\SEVEN\Desktop\test1.fasta'
    fasta(in1,in2,out1)
    print('测试3')
def id_wash(in1,in2,out1):
    '''
    根据特定基因命名，重新给蛋白文件的ID命名,并输出fasta格式文件
    :param in1:输入你的总序列库(fasta、fas、fa)（文件目录）
    :param in2:按行读取序列以>分隔并返回列表（文件目录）
    :param out1:输入你的基因号文件（格式：基因id 基因命名）示例：Solyc00g005000.2.1	NUX1（文件目录）
    :return:
    '''
    with open(in1)as pro_file: # 输入你的总序列库(fasta、fas、fa)
        pro_list=pro_file.read().split(">")                 # 按行读取序列以>分隔并返回列表
    with open(in2) as pro_txt:  # 输入你的基因号文件（格式基因id 基因命名）
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
    with open(out1,'w',encoding='UTF-8') as f1:
        for name in seq_out:
            '''
            输出数据清洗后的fasta文件到ceshi.fasta文件中
            '''
            if name:
                f1.write(name)
if __name__ =='main':
    in1=r'C:\Users\SEVEN\Desktop\fanqieceshi.fasta'
    in2=r'C:\Users\SEVEN\Desktop\1.txt'
    out1=r'C:\Users\SEVEN\Desktop\ceshi.fasta'
    id_wash(in1,in2,out1)
    print('测试4')
def motif(in1,in2,out1,out2):
    '''
    根据特定基因序列，提取存在该序列的fasta文件，并返回序列的匹配次数（文件目录）
    :param in1: 输入你的总序列库(fasta、fas、fa)（文件目录）
    :param in2: 输入特定基因序列（字符串形式基因序列）！一次只能放入一条序列
    :param out1: 将筛选出的基因ID和匹配次数以txt格式输出到目的文件中去（文件目录）
    :param out2:将根据特定基因序列筛选出的基因序列以fasta格式输出到目标文件中去（文件目录）
    :return:
    '''
    with open(in1) as seq_file: # 输入你的总序列库(fasta、fas、fa)
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
            reg = re.compile('{}'.format(in2).strip())              # 要匹配的特定基因序列
            result = reg.findall(seq_fa,re.I)       # 要匹配的特定基因序列(忽略大小写)
            if result:
                seq_num = str(len(result))
                seq_list1.append(">" + seq_name + "\t"+'(' + seq_num + ')' + "\n") # 导出对应的基因ID以及匹配次数
                seq_list2.append(">" + seq_name + "\n" + seq_fa + "\n")            # 拼接基因ID和基因序列
    print(seq_list1)                                 # 输出seq_list1以查看是否匹配到
    '''
    将筛选出的基因ID和匹配次数以txt格式输出到test1文件中去
    '''
    with open(out1, 'w', encoding='UTF-8') as f1:
        for name in seq_list1:
            if name:
                f1.write(name)
    '''
    将根据特定基因序列筛选出的基因序列以fasta格式输出到test4文件中去
    '''
    with open(out2,'w',encoding='UTF-8') as f2:
        for xulie in seq_list2:
            if xulie:
                f2.write(xulie)
if __name__ =='main':
    in1=r"C:\Users\SEVEN\Desktop\osa.fa"
    in2='TTAGGG'
    out1=r'C:\Users\SEVEN\Desktop\test3.txt'
    out2=r'C:\Users\SEVEN\Desktop\test4.fasta'
    motif(in1,in2,out1,out2)
    print('测试5')
def gsds(in1,in2,out1,out2):
    '''
    将gff格式的文件，转化为适合用于GSDS分析的BED格式文件
    :param in1: 输入你的总序列库(fasta、fas、fa)（文件目录）
    :param in2: 输入你的基因号文件（文件目录）
    :param out1: 输出BED格式的文件到bed.txt文件中（mRNA变成gene）（文件目录）
    :param out2: 输出BED格式的文件到bed.txt文件中（选出特定的位置，cds、gene[原mRNA]）（文件目录）
    :return:
    '''
    with open(in1)as gff_file: # 输入你的总序列库(fasta、fas、fa)
        gff_list=gff_file.readlines()                # 按行读取序列返回列表
    with open(in2) as gff_txt:  # 输入你的基因号文件
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
    with open(out1,'w',encoding='UTF-8') as f1:
        for seq in gff_list1:
            '''
            输出BED格式的文件到bed.txt文件中
            '''
            if seq:
                f1.write(seq)
    with open(out2,'w',encoding='UTF-8') as f2:
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
if __name__ =='main':
    in1=r"C:\Users\SEVEN\Desktop\ath.gff"
    in2=r"C:\Users\SEVEN\Desktop\1.txt"
    out1=r'C:\Users\SEVEN\Desktop\bed1.txt'
    out2=r'C:\Users\SEVEN\Desktop\bed2.txt'
    gsds(in1,in2,out1,out2)
    print('测试6')
def gff(in1,in2,out1):
    '''
    根据基因id提取gff文件
    :param in1: 输入你的基因注释gff文件(文件目录)
    :param in2: 输入你的基因号文件(文件目录)
    :param out1: 将根据基因ID筛选出的基因注释输出到test1文件中去(文件目录)
    :return:
    '''
    with open(in1) as gff_file:  # 输入你的基因注释文件(gff)
        gff_list=gff_file.readlines()                     # 按行读取序列返回列表
    with open(in2) as gff_txt: # 输入你的基因号文件
        seq_id = gff_txt.read().split('\n')               # 将基因ID以\n分隔开
    gff_out=[]
    for gff in gff_list:
        '''
        根据特定基因ID，提取基因注释文件
        '''
        for name in seq_id:
            if gff.startswith('#'):
                continue
            else:
                gff_list = gff.split('\t')
                ID = gff_list[-1]
                reg = re.compile('{}'.format(name))
                result = reg.findall(ID)
                if result:
                    gff_out.append(gff)

    # print(gff_out)                                      # 输出提取出来的基因或的蛋白序列
    '''
    将根据基因ID筛选出的基因注释输出到test1文件中去
    '''
    with open(out1,'w',encoding='UTF-8') as f1:
        for seq in gff_out:
            if seq:
                f1.write(seq)
if __name__ =='main':
    in1=r"C:\Users\SEVEN\Desktop\ath.gff"
    in2=r"C:\Users\SEVEN\Desktop\1.txt"
    out1=r'C:\Users\SEVEN\Desktop\test1.gff'
    gff(in1,in2,out1)
    print('测试7')