3# 常用命令

## 常用bash

[sed](#sed)
[awk](#awk)
[cut](#cut)
[sort](#sort)
[uniq](#uniq)
[grep](#grep)
[tr](#tr)
[wc](#wc)
[netstat](#netstat)
[free](#free)
[ps](#ps)
[top](#top)
[curl](#curl)

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
13. [求平均值](#13)
14. [去掉所有包含span的句子](#14)
15. [去掉不需要的单词](#15)
16. [有效电话号码](#16)

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
#       -n 多行输出 num [几列]
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

### <span id = "13">13. 求平均值</span>

```bash
#!/bin/sh
# 写一个bash脚本以实现一个需求，求输入的一个的数组的平均值
# (保留小数点后面3位)

awk 'BEGIN{sum=0;}{if(NR!=1){sum+=$1;}}END{printf("%.3f\n",sum/(NR-1))}' nowcoder.txt
# 第1行为输入的数组长度N
# 第2~N行为数组的元素，如以下为:
# 数组长度为2，数组元素为1 2
# 示例:
# 2
# 1
# 2
# 那么平均值为:1.500(保留小数点后面3位)
```


### <span id = "14">14. 去掉所有包含span的句子</span>

```bash
#!/bin/sh
# 去掉所有包含this的句子

# grep -v 显示不包含匹配文本的所有行
grep -v 'span' README.md
# awk 命令,检查当前 $0 不包含 this 并输出
awk '$0!~/this/ {print $0}'
```


### <span id = "15">15. 去掉不需要的单词</span>

```bash
#!/bin/sh
# 写一个 bash脚本以实现一个需求，去掉输入中的含有B和b的单词
grep -v -E 'b|B' README.md
grep -iv "b" $1
grep -v '[bB]' $1

cat nowcoder.txt | grep -v -E 'b|B' 

awk '$0!~/b|B/ {print $0}' README.md
awk '!/[bB]/'
```

### <span id = "16">16. 有效电话号码</span>

```bash
#!/bin/sh
# 一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx
grep -P '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt

awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt
```

9\10

### <span id = "sed">sed</span>

```bash
Edit text in a scriptable manner.

- Replace the first occurrence of a string in a file, and print the result:
    sed 's/find/replace/' filename

- Replace all occurrences of an extended regular expression in a file:
    sed -E 's/regex/replace/g' filename

- Replace all occurrences of a string in a file, overwriting the file (i.e. in-place):
    sed --in-place='' 's/find/replace/g' filename

- Replace only on lines matching the line pattern:
    sed '/line_pattern/s/find/replace/' filename

- Print only text between n-th line till the next empty line:
    sed -n 'line_number,/^$/p' filename

- Apply multiple find-replace expressions to a file:
    sed -e 's/find/replace/' -e 's/find/replace/' filename

- Replace separator / by any other character not used in the find or replace patterns, e.g., #:
    sed 's#find#replace#' filename
```

### <span id = "awk">awk</span>

```bash
A versatile programming language for working on files.
More information: <https://github.com/onetrueawk/awk>.

- Print the fifth column (a.k.a. field) in a space-separated file:
    awk '{print $5}' filename

- Print the second column of the lines containing "something" in a space-separated file:
    awk '/something/ {print $2}' filename

- Print the last column of each line in a file, using a comma (instead of space) as a field separator:
    awk -F ',' '{print $NF}' filename

- Sum the values in the first column of a file and print the total:
    awk '{s+=$1} END {print s}' filename

- Sum the values in the first column and pretty-print the values and then the total:
    awk '{s+=$1; print $1} END {print "--------"; print s}' filename

- Print every third line starting from the first line:
    awk 'NR%3==1' filename

- Print all values starting from the third column:
    awk '{for (i=3; i <= NF; i++) printf $i""FS; print""}' filename

- Print different values based on conditions:
    awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' filename
```

### <span id = "cut">cut</span>

```bash
Cut out fields from `stdin` or files.

- Cut out the first sixteen characters of each line of `stdin`:
    cut -c 1-16

- Cut out the first sixteen characters of each line of the given files:
    cut -c 1-16 file

- Cut out everything from the 3rd character to the end of each line:
    cut -c 3-

- Cut out the fifth field of each line, using a colon as a field delimiter (default delimiter is tab):
    cut -d':' -f5

- Cut out the 2nd and 10th fields of each line, using a semicolon as a delimiter:
    cut -d';' -f2,10

- Cut out the fields 3 through to the end of each line, using a space as a delimiter:
    cut -d' ' -f3-
```

### <span id = "sort">sort</span>

```bash
Sort lines of text files.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

- Sort a file in ascending order:
    sort path/to/file

- Sort a file in descending order:
    sort -r path/to/file

- Sort a file in case-insensitive way:
    sort --ignore-case path/to/file

- Sort a file using numeric rather than alphabetic order:
    sort -n path/to/file

- Sort the passwd file by the 3rd field, numerically:
    sort -t: -k 3n /etc/passwd

- Sort a file preserving only unique lines:
    sort -u path/to/file

- Sort human-readable numbers (in this case the 5th field of `ls -lh`):
    ls -lh | sort -h -k 5

- Sort numbers with exponents:
    sort --general-numeric-sort path/to/file
```

### <span id = "uniq">uniq</span>

```bash
Output the unique lines from the given input or file.
Since it does not detect repeated lines unless they are adjacent, we need to sort them first.

- Display each line once:
    sort file | uniq

- Display only unique lines:
    sort file | uniq -u

- Display only duplicate lines:
    sort file | uniq -d

- Display number of occurrences of each line along with that line:
    sort file | uniq -c

- Display number of occurrences of each line, sorted by the most frequent:
    sort file | uniq -c | sort -nr
```

### <span id = "grep">grep</span>

```bash
Matches patterns in input text.
Supports simple patterns and regular expressions.

- Search for a pattern within a file:
    grep search_pattern path/to/file

- Search for an exact string:
    grep -F exact_string path/to/file

- Search for a pattern [R]ecursively in the current directory, showing matching line [n]umbers, [I]gnoring non-text files:
    grep -RIn search_pattern .

- Use extended regular expressions (supporting `?`, `+`, `{}`, `()` and `|`), in case-insensitive mode:
    grep -Ei search_pattern path/to/file

- Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:
    grep -C|B|A 3 search_pattern path/to/file

- Print file name with the corresponding line number for each match:
    grep -Hn search_pattern path/to/file

- Use the standard input instead of a file:
    cat path/to/file | grep search_pattern

- Invert match for excluding specific strings:
    grep -v search_pattern
```

### <span id = "tr">tr</span>

```bash
Translate characters: run replacements based on single characters and character sets.

- Replace all occurrences of a character in a file, and print the result:
    tr find_character replace_character < filename

- Replace all occurrences of a character from another command's output:
    echo text | tr find_character replace_character

- Map each character of the first set to the corresponding character of the second set:
    tr 'abcd' 'jkmn' < filename

- Delete all occurrences of the specified set of characters from the input:
    tr -d 'input_characters' < filename

- Compress a series of identical characters to a single character:
    tr -s 'input_characters' < filename

- Translate the contents of a file to upper-case:
    tr "[:lower:]" "[:upper:]" < filename

- Strip out non-printable characters from a file:
    tr -cd "[:print:]" < filename
```

### <span id = "wc">wc</span>

```bash
Count lines, words, or bytes.

- Count lines in file:
    wc -l file

- Count words in file:
    wc -w file

- Count characters (bytes) in file:
    wc -c file

- Count characters in file (taking multi-byte character sets into account):
    wc -m file

- Use standard input to count lines, words and characters (bytes) in that order:
    find . | wc
```

### <span id = "netstat">netstat</span>

```bash
Displays network-related information such as open connections, open socket ports, etc.

- List all ports:
    netstat -a

e.g
netstat -a
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  172.21.194.30.53645    114.55.207.244.https   ESTABLISHED

- List all listening ports:
    netstat -l

- List listening TCP ports:
    netstat -t

- Display PID and program names for a specific protocol:
    netstat -p protocol

- Print the routing table:
    netstat -nr
```

### <span id = "free">free</span>

```bash
Display amount of free and used memory in the system

free [-b | -k | -m] [-o] [-s delay ] [-t] [-l] [-V]

The -b switch displays the amount of memory in bytes; the -k switch (set
by default) displays it in kilobytes;  the  -m  switch  displays  it  in
megabytes.

The -t switch displays a line containing the totals.

The  -o switch disables the display of a "buffer adjusted" line.  If the
-o option is not specified, free subtracts buffer memory from  the  used
memory and adds it to the free memory reported.

The  -s switch activates continuous polling delay seconds apart. You may
actually specify any floating point number for delay, usleep(3) is  used
for microsecond resolution delay times.

The -l switch shows detailed low and high memory statistics.

The -V switch displays version information.
```

### <span id = "ps">ps</span>

```bash
Information about running processes.

- List all running processes:
    ps aux

e.g
USER PID %CPU %MEM VSZ RSS TT STAT STARTED TIME COMMAND

- List all running processes including the full command string:
    ps auxww

- Search for a process that matches a string:
    ps aux | grep string

- List all processes of the current user in extra full format:
    ps --user $(id -u) -F

- List all processes of the current user as a tree:
    ps --user $(id -u) f

- Get the parent pid of a process:
    ps -o ppid= -p pid

- Sort processes by memory consumption:
    ps --sort size
```

### <span id = "top">top</span>

```bash
Display dynamic real-time information about running processes.

- Start top, all options are available in the interface:
    top
e.g.
Processes: xx total, 3 running, xx sleeping, xx threads                                                       
Load Avg: 2.28, 2.30, 2.14  CPU usage: 11.79% user, 7.5% sys, 81.15% idle
SharedLibs: xxM resident, 39M data, 29M linkedit. MemRegions: xx total, xxM resident, 64M private, xxM shared.
PhysMem: xxM used (xxM wired), 68M unused.
VM: xxG vsize, xxM framework vsize, xx(xx) swapins, xx(0) swapouts.
Networks: packets: xx/xxM in, xx/xxM out. Disks: xx/xxG read, xx/xxG written.

PID COMMAND %CPU TIME #TH #WQ #PORTS MEM PURG CMPRS PGRP PPID STATE BOOSTS %CPU_ME


- Start top sorting processes by internal memory size (default order - process ID):
    top -o mem

- Start top sorting processes first by CPU, then by running time:
    top -o cpu -O time

- Start top displaying only processes owned by given user:
    top -user user_name

- Get help about interactive commands:
    ?
```

### <span id = "curl">curl</span>

```bash
Transfers data from or to a server.
Supports most protocols, including HTTP, FTP, and POP3.
More information: <https://curl.haxx.se>.

- Download the contents of an URL to a file:
    curl http://example.com -o filename

- Download a file, saving the output under the filename indicated by the URL:
    curl -O http://example.com/filename

- Download a file, following [L]ocation redirects, and automatically [C]ontinuing (resuming) a previous file transfer:
    curl -O -L -C - http://example.com/filename

- Send form-encoded data (POST request of type `application/x-www-form-urlencoded`). Use `-d @file_name` or `-d @'-'` to read from STDIN:
    curl -d 'name=bob' http://example.com/form

- Send a request with an extra header, using a custom HTTP method:
    curl -H 'X-My-Header: 123' -X PUT http://example.com

- Send data in JSON format, specifying the appropriate content-type header:
    curl -d '{"name":"bob"}' -H 'Content-Type: application/json' http://example.com/users/1234

- Pass a user name and password for server authentication:
    curl -u myusername:mypassword http://example.com

- Pass client certificate and key for a resource, skipping certificate validation:
    curl --cert client.pem --key key.pem --insecure https://example.com
```
