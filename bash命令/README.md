# 常用命令

## 常用脚本

1. [获取文件行数](#1)
2. [打印文件的最后5行](#1)
3. [输出7的倍数](#3)
4. [输出第5行的内容](#4)
5. [打印空行的行号](#5)
6. [去掉空行](#6)
7. [打印字母数小于8的单词](#7)
8. [统计所有进程占用内存大小的和](#8)
9. [统计每个单词出现的个数](#9)
10. [第二列是否有重复](#10)
11. [转置文件的内容](#11)
12. [打印每一行出现的数字个数](#12)
13. [去掉所有包含span的句子](#13)
14. [求平均值](#14)
15. [去掉所有包含span的句子](#15)

### <span id = "1">1. 获取文件行数</span>

```bash
#!/bin/sh
# 统计文件行数

#awk NR
awk '{print NR}' README.md |tail -n1
awk 'END{print NR}' README.md
# grep -n "" README.md |awk -F: '{print '} |tail -n1
grep -n "" README.md | awk -F: '{print '} |tail -n1 | cut -d ":" -f 1
sed -n '$=' README.md
#wc -l
# 计算少1，是因为文件是由Windows下生成,文件最后一行不会自动增加'\n'换行符
cat README.md | wc -l
```

### <span id = "2">2. 打印文件的最后5行</span>

```bash
#!/bin/sh
# 打印文件的最后5行

tail -5 README.md
```

### <span id = "3">3. 输出7的倍数</span>

```bash
#!/bin/sh
# 打印文件的最后5行一个 bash脚本以输出数字 0 到 500 中 7 的倍数(0 7 14 21...)的命令

#seq 用于生成从一个数到另一个数之间的所有整数。
#用法：seq [选项]... 尾数
#  或：seq [选项]... 首数 尾数
#  或：seq [选项]... 首数 增量 尾数
seq 0 7 500

# or
for i in {0..500}
    do
        if [[ i%7 -eq 0 ]];then
            echo $i
        fi
    done
```

### <span id = "4">4. 输出第5行的内容</span>

```bash
#!/bin/sh
# 输出第5行的内容

# head 从头开始打印，tail 从未开始打印，sed 从中间开始打印
# sed 命令中的 p 子命令，打印第五行
sed -n 5p README.md
# head 命令拿到前五行，再通过通道，通过tail取出来最后一行，即第五行
head -n 5 README.md | tail -n 1
```

### <span id = "5">5. 打印空行的行号</span>

```bash
#!/bin/sh
# 打印空行的行号

# -n 对匹配的行做处理
# = 打印匹配到的内容的行号
# p 打印匹配到的内容
sed -n '/^$/=' README.md
# or
grep -n "^$" README.md | cut -d ":" -f 1
grep -n ' ' README.md | awk -F : '{print $1}'
# or
awk '/^$/{print NR}' README.md
```

### <span id = "6">6. 去掉空行</span>

```bash
#!/bin/sh
# 去掉空行

# cat 输出文本内容，然后通过管道符交由 awk 做非空校验然后输出
cat README.md | awk NF

# grep -v 显示不包含匹配文本的所有行
grep -v '^$' README.md
# grep -e 指定字符串做为查找文件内容的样式
grep -e '\S' README.md

# awk
awk '!/^$/ {print $NF}' README.md
awk '{if($0 != "") {print $0}}' README.md
```

### <span id = "7">7. 打印字母数小于8的单词</span>

```bash
#!/bin/sh
# 打印字母数小于8的单词

# xargs 给其它命令传递参数的一个过滤器
#       -n 多行输出 num [一行展示几个元素]
cat README.md | xargs -n3 | awk 'length($1)<8 {print $1}'

# awk
awk '{for(i=1;i<=NF;i++){if(length($i)<8){print $i}}}' README.md
```

### <span id = "8">8. 统计所有进程占用内存大小的和</span>

```bash
#!/bin/sh
# 统计所有进程占用内存大小的和
# ps aux | grep -v 'RSS TTY' > demo.txt

awk '{a+=$6}END{print a}' demo.txt

# USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
# USER 进程的属主
# PID 进程的ID
# %CPU 进程占用的CPU百分比
# %MEM 占用内存的百分比
# VSZ 进程使用的虚拟內存量（KB）
# RSS 该进程占用的固定內存量（KB）（驻留中页的数量）
```

### <span id = "9">9. 统计每个单词出现的个数</span>

```bash
#!/bin/sh
# 统计每个单词出现的个数

# right
cat README.md | xargs -n 1 | sort | uniq -c | sort -n | awk '{print $2,$1}'
```

### <span id = "10">10. 第二列是否有重复</span>

```bash
#!/bin/sh
# 第二列是否有重复

cat $1 | awk '{print $2}' | sort | uniq -c | sort | grep -v 1
```

### <span id = "11">11. 转置文件的内容</span>

```bash
#!/bin/sh
# 转置文件的内容
# 假设每行列数相同，并且每个字段由空格分隔

awk '{
    for(i=1;i<=NF;i++){rows[i]=rows[i]" "$i}
} END{
    for(line in rows){print rows[line]}
}' nowcoder.txt

# 示例:
# 假设 nowcoder.txt 内容如下：
# job salary
# c++ 13
# java 14
# php 12

# 你的脚本应当输出（以词频升序排列）：
# job c++ java php
# salary 13 14 12
```

### <span id = "12">12. 打印每一行出现的数字个数</span>

```bash
#!/bin/sh
# 打印每一行出现的数字个数
# 写一个 bash脚本以统计一个文本文件 nowcoder.txt中每一行出现的1,2,3,4,5数字个数并且要计算一下整个文档中一共出现了几个1,2,3,4,5数字数字总数

# 利用 awk 的 gsub 返回替换的数量
awk '{
    num = gsub(/[1-5]/, "");
    sum += num;
    printf("line%d number: %d\n", NR, num);
}
END {
    printf("sum is %d\n", sum);
}' README.md
```

### <span id = "13">13. 去掉所有包含span的句子</span>

```bash
#!/bin/sh
# 去掉所有包含this的句子

# grep -v 显示不包含匹配文本的所有行
grep -v 'span' README.md
# awk 命令,检查当前 $0 不包含 this 并输出
awk '$0!~/this/ {print $0}'
```

### <span id = "13">13. 去掉所有包含span的句子</span>

```bash
#!/bin/sh
# 写一个bash脚本以实现一个需求，求输入的一个的数组的平均值
# (保留小数点后面3位)

awk 'BEGIN{sum=0;}{if(NR!=1){sum+=$1;}}END{printf("%.3f\n",sum/(NR-1))}' nowcoder.txt
```

### <span id = "14">14. 求平均值</span>

```bash
#!/bin/sh
# 求平均值

awk 'BEGIN{sum=0;}{if(NR!=1){sum+=$1;}}END{printf("%.3f\n",sum/(NR-1))}' nowcoder.txt
# 第1行为输入的数组长度N
# 第2~N行为数组的元素，如以下为:
# 数组长度为2，数组元素为1 2
# 示例:
# 4
# 1
# 2
# 那么平均值为:1.500(保留小数点后面3位)
```

### <span id = "15">15. 去掉所有包含span的句子</span>

```bash
#!/bin/sh
# 去掉不需要的单词
grep -v -E 'b|B' README.md
grep -iv "b" $1
grep -v '[bB]' $1

cat nowcoder.txt | grep -v -E 'b|B' 

awk '$0!~/b|B/ {print $0}' README.md
awk '!/[bB]/'
```

9\10