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



### <span id = "1">1. 获取文件行数</span>

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

### 

[题目链接](https://www.nowcoder.com/ta/sql)
