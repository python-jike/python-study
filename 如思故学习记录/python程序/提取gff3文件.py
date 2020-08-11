import re
gff_file=open(r"C:\Users\SEVEN\Desktop\ath.gff")  # 输入你的基因注释文件(gff)
gff_list=gff_file.readlines()                     # 按行读取序列返回列表
gff_txt = open(r"C:\Users\SEVEN\Desktop\1.txt")   # 输入你的基因号文件
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

#print(gff_out)                                      # 输出提取出来的基因或的蛋白序列
'''
将根据基因ID筛选出的基因注释输出到test1文件中去
'''
f1=open(r'C:\Users\SEVEN\Desktop\test1.gff','w',encoding='UTF-8')
for seq in gff_out:
    if seq:
        f1.write(seq)
f1.close()
gff_txt.close()
gff_file.close()