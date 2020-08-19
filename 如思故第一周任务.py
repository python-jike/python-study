import os,shutil
c1=[]
c2=[]
c3=[]
with open(r'C:\Users\SEVEN\Desktop\1.txt') as a:
    '''
    读取1.txt文件，输出到列表a1中
    '''
    a1=a.readlines()
print(a1)
with open(r'C:\Users\SEVEN\Desktop\2.txt') as b:
    '''
    读取2.txt文件，输出到列表a2中
    '''
    b1=b.readlines()
print(b1)
for i,j in zip(a1,b1):
    '''
    将两个文件内容交替输出到列表c1中，最终输出到3.txt中
    '''
    c1.append(i.strip())
    c1.append(j.strip())
print(c1)
with open(r'C:\Users\SEVEN\Desktop\3.txt','w') as d1:
    for k in c1:
        if k == c1[-1]:
            d1.write(k)
        else:
            d1.write(k + '\n')
for i,j in zip(a1,b1):
    '''
    将两个文件的每行字符串相加, 输出到列表c2中，最终输出到4.txt中
    '''
    c=str(i).strip()+str(j).strip()
    c2.append(c)
print(c2)
with open(r'C:\Users\SEVEN\Desktop\4.txt','w') as d2:
    for k in c2:
        if k==c2[-1]:
            d2.write(k)
        else:
            d2.write(k+'\n')
for i, j in zip(a1, b1):
    '''
    将两个文件的每行数字和相加, 输出到列表c3中，最终输出到5.txt中
    '''
    c = int(i.strip())+int(j.strip())
    c3.append(str(c))
print(c3)
with open(r'C:\Users\SEVEN\Desktop\5.txt','w') as d3:
    for k in c3:
        if k == c3[-1]:
            d3.write(k)
        else:
            d3.write(k + '\n')
# 将3.txt文件中内容输出到6.txt中。
with open(r'C:\Users\SEVEN\Desktop\3.txt') as d4:
    a3=d4.readlines()
with open(r'C:\Users\SEVEN\Desktop\6.txt', 'w') as d5:
    for k in a3:
        d5.write(k)
# 利用shutil模块备份文件到新路径
shutil.copyfile(r'C:\Users\SEVEN\Desktop\3.txt',r'C:\Users\SEVEN\Desktop\programing-book\6.txt')
