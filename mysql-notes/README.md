# mysql-notes

* 四十五讲
* 必知必会


## 索引

### 索引的常见模型

* 哈希表
* 有序数组
* 搜索树
    - 二叉搜索树：每个节点的左儿子小于父节点，父节点又小于右儿子
    - 多叉树：每个节点有多个儿子，儿子之间的大小保证从左到右 递增

## demo

1. [查找最晚入职员工的所有信息 - order by](#1)
2. [查找当前薪水详情以及部门编号dept_no - inner join](#2)
3. [查找所有已经分配部门的员工的last_name和first_name以及dept_no](#3)
4. [查找所有员工的last_name和first_name以及对应部门编号dept_no - left join](#4)
5. [查找薪水记录超过15次的员工号emp_no以及其对应的记录次数t - group by having](#5)
6. [找出所有员工当前薪水salary情况 - distinct / group by](#6)
7. [获取所有非manager的员工emp_no - 子查询 / is null](#7)
8. [获取所有员工当前的manager](#8)
9. [获取每个部门中当前员工薪水最高的相关信息](#9)
10. [条件查找employees表](#10)
11. [统计出当前各个title类型对应的员工当前薪水对应的平均工资](#11)
12. [获取当前薪水第二多的员工的emp_no以及其对应的薪水salary - group by](#12)
13. [获取当前薪水第二多的员工的emp_no以及其对应的薪水salary - max](#13)
14. [查找所有员工的last_name和first_name以及对应的dept_name - 三表查询](#14)
15. [统计各个部门的工资记录数 - 三表查询](#15)
16. [对所有员工的薪水按照salary进行按照1-N的排名 - 自连接 / count group by](#16)
17. [获取所有非manager员工当前的薪水情况 - 四表查询](#17)
18. [获取员工其当前的薪水比其manager当前薪水还高的相关信息](#18)
19. [汇总各个部门当前员工的title类型的分配数目 - group by 多字段](#19)
20. [查找描述信息中包含robot的电影对应的分类名称以及电影数目，而且还需要该分类对应电影数量>=5部 - like %xx%](#20)
21. [使用join查询方式找出没有分类的电影id以及名称 - 处理相关table](#21)
22. [使用子查询的方式找出属于Action分类的所有电影对应的title,description](#22)
23. [字段名拼接 concat_ws](#23)
24. [创建一个actor表 - create](#24)
25. [MYSQL创建数据表的三种方法 - create](#25)
26. [批量插入数据 - insert](#26)
27. [批量插入数据，不使用replace操作 - insert ignore](#27)
28. [对first_name创建唯一索引uniq_idx_firstname - unique / index](#28)
29. [针对actor表创建视图actor_name_view - view as](#29)
30. [查询emp_no为10005, 使用强制索引 - force index](#30)
31. [新增列 - alter add](#31)
32. [删除emp_no重复的记录，只保留最小的id对应的记录- delete](#32)
33. [数据更新 - update [repalce]](#33)
34. [将titles_test表名修改为titles_2017 - alter rename](#34)
35. [将所有获取奖金的员工当前的薪水增加10% - update](#35)
36. [分页查询employees表 - limit](#36)
37. [使用含有关键字exists查找未分配具体部门的员工的所有信息 - select exists](#37)
38. [每个人最近的登录日期 - select](#38)



### <span id = "1">1. 查找最晚入职员工的所有信息</span>

```sql
-- ORDER BY 根据指定的列对结果集进行排序，默认按照升序，降序 ORDER BY DESC
-- LIMIT(m, n) 从第 m + 1 行开始取 n 条记录
-- 最晚员工自然是 hire_data，最晚可以用排序 ORDER BY DESC 降序来得到，然后是获取第一条记录，这样理论上是有 bug 的，因为 hire_data 可能有多个相同的记录
SELECT * FROM employees order by hire_date desc limit 0,1

-- 使用子查询，最后一天的时间有多个员工信息
SELECT * FROM employees WHERE hire_date == (SELECT MAX(hire_date) FROM employees)
```

### <span id = "2">2. 查找当前薪水详情以及部门编号dept_no</span>

```sql
-- 左右连接
-- 左外部联结（LEFT JOIN）- 包含左边表的所有列
-- 右外部联结（RIGHT JOIN）- 包含右边表的所有列
-- 内部联结（INNER JOIN）- select 选中的列
select s.*,d.dept_no
from salaries as s inner join dept_manager as d
on s.emp_no=d.emp_no
where s.to_date='9999-01-01' and d.to_date='9999-01-01'
```

### <span id = "3">3. 查找所有已经分配部门的员工的last_name和first_name以及dept_no</span>

```sql
select s.last_name, s.first_name, d.dept_no
from employees as s inner join dept_emp as d
on s.emp_no = d.emp_no
where d.dept_no is not NULL
```

### <span id = "4">4. 查找所有员工的last_name和first_name以及对应部门编号dept_no</span>

```sql
select s.last_name, s.first_name, d.dept_no
from employees as s left join dept_emp as d
on s.emp_no = d.emp_no
```

### <span id = "5">5. 查找薪水记录超过15次的员工号emp_no以及其对应的记录次数t</span>

```sql

-- 分组+聚合函数
-- group by语法：
-- SELECT column_1, column_2, … column_n, aggregate_function(expression), constant
-- FROM tables
-- WHERE predicates
-- GROUP BY column_1, column_2, … column_n
-- HAVING condition_1 … condition_n;
-- 注意：因为聚合函数通过作用一组值而只返回一个单一值，因此，在SELECT语句中出现的字段要么为一个聚合函数的输入值，如COUNT(course)，要么为GROUP BY语句中指定的字段，要么是常数，否则会出错。
-- 简而言之：使用GROUP BY子句时，SELECT子句中只能有聚合键、聚合函数、常数。
select emp_no, count(emp_no) as t from salaries group by emp_no having t > 15

select number from grade group by number having count(*)>=3
```

### <span id = "6">6. 找出所有员工当前薪水salary情况</span>

```sql
-- 对于distinct与group by的使用：
-- 1.当对系统的性能高并且数据量大时使用group by
-- 2.当对系统的性能不高时或者使用数据量少时两者借口
-- 3.尽量使用group by
select distinct salary from salaries order by salary desc
-- WHERE语句在GROUP BY语句之前，SQL会在分组之前计算WHERE语句。HAVING语句在GROUP BY语句之后，SQL会在分组之后计算HAVING语句
select salary from salaries group by salary order by salary desc
```

### <span id = "7">7. 获取所有非manager的员工emp_no</span>

```sql
-- NOT IN+子查询
select emp_no from employees where emp_no not in (select emp_no from dept_manager)
-- LEFT JOIN左连接+IS NULL
select e.emp_no from employees as e left join dept_manager as d on e.emp_no=d.emp_no where dept_no is null
```

### <span id = "8">8. 获取所有员工当前的manager</span>

```sql
select de.emp_no, dm.emp_no as manager_no 
from dept_emp as de inner join dept_manager as dm 
on de.dept_no=dm.dept_no
where de.emp_no != dm.emp_no
```

### <span id = "9">9. 获取每个部门中当前员工薪水最高的相关信息</span>

```sql

SELECT d1.dept_no, d1.emp_no, s1.salary
FROM dept_emp as d1
INNER JOIN salaries as s1
ON d1.emp_no=s1.emp_no
WHERE s1.salary in (SELECT MAX(s2.salary)
                    FROM dept_emp as d2
                    INNER JOIN salaries as s2
                    ON d2.emp_no=s2.emp_no
                    AND d2.dept_no = d1.dept_no)
ORDER BY d1.dept_no;
```

### <span id = "10">10. 条件查找employees表</span>

```sql
-- employees表所有emp_no为奇数，且last_name不为Mary的员工信息，并按照hire_date逆序排列
select * from employees where emp_no%2!=0 and last_name!="Mary" order by hire_date desc;
```

### <span id = "11">11. 统计出当前各个title类型对应的员工当前薪水对应的平均工资</span>

```sql
select t.title, avg(salary)
from titles as t
inner join salaries as s
on t.emp_no=s.emp_no
group by t.title
```

### <span id = "12">12. 获取当前薪水第二多的员工的emp_no以及其对应的薪水salary</span>

```sql
select emp_no, salary 
from salaries 
where salary = (select salary 
                from salaries 
                group by salary 
                order by salary desc limit 1,1)
```

### <span id = "13">13. 获取当前薪水第二多的员工的emp_no以及其对应的薪水salary</span>

```sql
select s.emp_no, s.salary, e.last_name, e.first_name
from salaries s join employees e
on s.emp_no = e.emp_no
where s.salary =            -- 第三步: 将第二高工资作为查询条件
    (select max(salary)     -- 第二步: 查出除了原表最高工资以外的最高工资(第二高工资)
    from salaries 
    where salary < (
        select max(salary)  -- 第一步: 查出原表最高工资
        from salaries
        )
    )
```

### <span id = "14">14. 查找所有员工的last_name和first_name以及对应的dept_name</span>

```sql
-- 三表查询
select last_name, first_name, dept_name 
from employees
left join dept_emp on employees.emp_no=dept_emp.emp_no
left join departments on dept_emp.dept_no=departments.dept_no
```

### <span id = "15">15. 统计各个部门的工资记录数</span>

```sql
SELECT d.dept_no, d.dept_name, COUNT(*) AS sum
FROM departments AS d, dept_emp AS de, salaries AS s
WHERE d.dept_no=de.dept_no
AND de.emp_no=s.emp_no
GROUP BY d.dept_no order by d.dept_no;
```

### <span id = "16">16. 对所有员工的薪水按照salary进行按照1-N的排名 - 自连接 / count group by</span>

```sql

SELECT s1.emp_no, s1.salary, COUNT(DISTINCT s2.salary) AS t_rank 
FROM salaries AS s1, salaries AS s2 
WHERE s1.salary <= s2.salary 
GROUP BY s1.emp_no 
ORDER BY s1.salary DESC, s1.emp_no ASC
```

### <span id = "17">17. 获取所有非manager员工当前的薪水情况 - 四表查询</span>

```sql
select de.dept_no,a.emp_no,s.salary
from (select emp_no
      from employees
      where emp_no not in (select emp_no
                           from dept_manager)
     ) as a
inner join dept_emp de on a.emp_no=de.emp_no
inner join salaries s on a.emp_no=s.emp_no
where s.to_date='9999-01-01'
```

### <span id = "18">18. 获取员工其当前的薪水比其manager当前薪水还高的相关信息</span>

```sql
select de.emp_no, dm.emp_no as manager_no, s1.salary as emp_salary, s2.salary as manager_salary
from dept_emp de,dept_manager dm,salaries s1,salaries s2
where de.dept_no=dm.dept_no and de.emp_no=s1.emp_no
and dm.emp_no=s2.emp_no and s1.salary>s2.salary
```

### <span id = "19">19. 汇总各个部门当前员工的title类型的分配数目 - group by 多字段</span>

```sql
-- group by 多字段
select d.dept_no, d.dept_name, t.title, count(t.title) as count
from departments d, dept_emp de, titles t
where de.emp_no=t.emp_no
and de.dept_no=d.dept_no
group by d.dept_no, t.title order by d.dept_no
```

### <span id = "20">20. 查找描述信息中包含robot的电影对应的分类名称以及电影数目，而且还需要该分类对应电影数量>=5部 - like %xx%</span>

```sql
select c.name, count(fc.film_id)
from film f, category c, film_category fc
where f.description like '%robot%'
and f.film_id=fc.film_id
and fc.category_id=c.category_id
and c.category_id in (select category_id
                      from film_category
                      group by category_id
                      having count(film_id)>=5)  -- having count
```

### <span id = "21">21. 使用join查询方式找出没有分类的电影id以及名称 - 处理相关table</span>

```sql
select f.film_id, f.title
from film f
left join film_category fc
on f.film_id=fc.film_id
where fc.category_id is null
```

### <span id = "22">22. 使用子查询的方式找出属于Action分类的所有电影对应的title,description</span>

```sql

select f.title, f.description
from film f
where f.film_id in (select fc.film_id 
                    from category c 
                    inner join film_category fc
                    on c.category_id=fc.category_id
                    where name="Action")
```

### <span id = "23">23. 将employees表的所有员工的last_name和first_name拼接起来作为Name - concat_ws</span>

```sql
select concat_ws(' ', last_name, first_name) as Name from employees

SELECT CONCAT(last_name,"'",first_name) FROM employees;
```

### <span id = "24">24. 创建一个actor表 - create</span>

```sql
-- 列表	         类型	     是否为NULL	  含义
-- actor_id	    smallint(5)	not null	主键id
-- first_name	varchar(45)	not null	名字
-- last_name	varchar(45)	not null	姓氏
-- last_update	date	    not null	日期

-- CREATE TABLE table_name (column_name column_type);
CREATE TABLE actor(
actor_id smallint(5) primary key,
first_name varchar(45) not null,
last_name varchar(45) not null,
last_update date not null);
```

### <span id = "25">25. MYSQL创建数据表的三种方法 - create</span>

```sql
-- 请你创建一个actor_name表，并且将actor表中的所有first_name以及last_name导入该表.

-- 常规创建
create table if not exists 目标表
-- 复制表格
create 目标表 like 来源表
-- 将table1的部分拿来创建table2
create table if not exists actor_name
(
first_name varchar(45) not null,
last_name varchar(45) not null
)
select first_name,last_name
from actor
```

### <span id = "26">26. 批量插入数据 - insert</span>

```sql
-- INSERT INTO table_name ( field1, field2,...fieldN ) VALUES ( value1, value2,...valueN ); 
insert into actor(actor_id, first_name, last_name, last_update)
values(1,'PENELOPE','GUINESS','2021-02-15 12:34:33'),
      (2,'NICK','WAHLBERG','2021-02-15 12:34:33');
```

### <span id = "27">27. 批量插入数据，不使用replace操作 - insert ignore</span>

```sql
-- 对于表actor插入如下数据,如果数据已经存在，请忽略(不支持使用replace操作)
insert ignore into actor values("3","ED","CHASE","2006-02-15 12:34:33");
```

### <span id = "28">28. 对first_name创建唯一索引uniq_idx_firstname - unique / index</span>

```sql

CREATE UNIQUE INDEX uniq_idx_firstname on actor (first_name);
CREATE INDEX idx_lastname ON actor (last_name);

-- mysql
-- 添加主键
ALTER TABLE tbl_name ADD PRIMARY KEY (col_list);
-- 该语句添加一个主键，这意味着索引值必须是唯一的，且不能为NULL。

-- 添加唯一索引
ALTER TABLE tbl_name ADD UNIQUE index_name (col_list);
-- 这条语句创建索引的值必须是唯一的。

-- 添加普通索引
ALTER TABLE tbl_name ADD INDEX index_name (col_list);
-- 添加普通索引，索引值可出现多次。

-- 添加全文索引
ALTER TABLE tbl_name ADD FULLTEXT index_name (col_list);
-- 该语句指定了索引为 FULLTEXT ，用于全文索引。

-- 删除索引的语法：
DROP INDEX index_name ON tbl_name;
-- 或者
ALTER TABLE tbl_name DROP INDEX index_name；
ALTER TABLE tbl_name DROP PRIMARY KEY;
```

### <span id = "29">29. 针对actor表创建视图actor_name_view - view as</span>

```sql
CREATE VIEW actor_name_view
AS 
SELECT first_name AS first_name_v, last_name AS last_name_v
FROM actor;
```

### <span id = "30">30. 查询emp_no为10005, 使用强制索引 - force index</span>

```sql
select *
from salaries
force index (idx_emp_no)
where emp_no=10005
```

### <span id = "31">31. 新增列 - alter add</span>

```sql
-- ALTER TABLE table_name ADD column_name datatype [after field];
alter table actor
add create_date datetime not null default "2020-10-01 00:00:00" after last_update;
```

### <span id = "32">32. 删除emp_no重复的记录，只保留最小的id对应的记录- delete</span>

```sql
DELETE FROM titles_test
WHERE id NOT IN(
    SELECT * FROM(
    SELECT MIN(id)
    FROM titles_test
    GROUP BY emp_no) a);  -- 把得出的表重命名那就不是原表了
```

### <span id = "33">33. 数据更新 - update [replace]</span>

```sql
-- 基本的数据更新语法，UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
update titles_test set to_date = null , from_date = '2001-01-01' where to_date = '9999-01-01'

-- 表更新语句结构 UPDATE 表名 SET 字段 = REPLACE(字段，原值，变值) WHERE 过滤条件
update titles_test set emp_no = replace(emp_no,10001,10005) where id = 5
```

### <span id = "34">34. 将titles_test表名修改为titles_2017 - alter</span>

```sql
-- ALTER TABLE 表名 RENAME TO/AS 新表名 更改表名语句结构
ALTER TABLE titles_test RENAME TO titles_2017
```

### <span id = "34">34. 外键约束，其emp_no对应employees_test表的主键id - alter</span>

```sql
-- 创建外键语句结构：
-- ALTER TABLE <表名>
-- ADD CONSTRAINT FOREIGN KEY (<列名>)
-- REFERENCES <关联表>（关联列）
ALTER TABLE audit
ADD CONSTRAINT FOREIGN KEY (emp_no)
REFERENCES employees_test(id);
```

### <span id = "35">35. 将所有获取奖金的员工当前的薪水增加10% - update</span>

```sql
-- 1.连接查询（先join两张表）
update salaries as s join emp_bonus as e on s.emp_no=e.emp_no
set salary=salary*1.1
where to_date='9999-01-01'

-- 2. 子查询（两次select）
update salaries
set salary=salary*1.1
where to_date='9999-01-01'
    and salaries.emp_no in(select emp_no from emp_bonus)

-- 比较：
-- 推荐使用连接查询（JOIN）
-- 连接查询不需要创建+销毁临时表，因此速度比子查询快。
```

### <span id = "36">36. 分页查询employees表 - limit</span>

```sql
SELECT *
FROM employees
LIMIT 5,5

-- LIMIT 语句结构： LIMIT X,Y 
-- Y ：返回几条记录
-- X：从第几条记录开始返回（第一条记录序号为0，默认为0）
```

### <span id = "37">37. 使用含有关键字exists查找未分配具体部门的员工的所有信息 - select exists</span>

```sql

select * from employees e
where not exists
(select emp_no from dept_emp d where d.emp_no = e.emp_no);
```

### <span id = "38">38. 每个人最近的登录日期 - select</span>

```sql

select user_id, MAX(date) as d from login group by user_id order by user_id

select user.name as u_n, client.name as c_n, login.date
from login 
join user on login.user_id=user.id
join client on login.client_id=client.id
where (login.user_id,login.date) in
    (select user_id,max(date) from login group by login.user_id )
order by user.name;

-- 留存率（第一天登录的新用户并且第二天也登录的用户）/（总用户）
select
round(count(distinct user_id)*1.0 / (select count(distinct user_id) from login), 3)
from login
where (user_id, date) in
    (select user_id, DATE_ADD(MIN(date),INTERVAL 1 DAY) from login group by user_id);

-- 查询每个日期登录新用户个数
-- 先得到所有日期表select distinct date from login;
-- 然后左连接新用户首次登陆的日期表(select user_id, min(date) first_date from login group by user_id);
-- 归类统计日期出现的次数.
select a.date, count(b.user_id) new
from (select distinct date from login) a
left join (select user_id, min(date) first_date from login group by user_id) b on a.date=b.first_date 
group by a.date order by a.date

```

```sql
SELECT id, job, score
FROM grade a
WHERE score> (SELECT ROUND(AVG(score),3)
              FROM grade b
              WHERE a.job = b.job)
ORDER BY a.id
-- 
select job ,
       floor((sum(1)+1)/2) as start,
       floor((sum(1)+2)/2) as end
from grade
group by job
order by job
```

### 

[题目链接](https://www.nowcoder.com/ta/sql)
