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
