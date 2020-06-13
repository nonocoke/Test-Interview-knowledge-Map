# python

## 1 生成器与迭代器

### 1.1 生成器

在Python中，一边循环一边计算的机制，称为生成器： generator 。

* 创建 generator 生成器方法 1：
    列表生成式 `[x*x for x in range(10)]` 中的 [] 改为()，就创建了一个生成器 `(x*x for x in range(10))`

* 创建 generator 生成器方法 2：
    例子：斐波拉契数列 用函数把它打印出来 如下

    ```python
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            print(b)
            a, b = b, a + b
            n = n + 1
        return 'done'
    ```

    可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

    也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把 print(b) 改为 yield b 就可以了。

    ```python
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'

    >>> f = fib(2)
    >>> f
    <generator object fib at 0x...>
    ```

    最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

    举个简单的例子，定义一个generator，依次返回数字1，3，5：

    ```python
    def odd():
        print('step 1')
        yield 1
        print('step 2')
        yield(3)
        print('step 3')
        yield(5)

    # 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
    >>> o = odd()
    >>> next(o)
    step 1
    1
    >>> next(o)
    step 2
    3
    >>> next(o)
    step 3
    5
    >>> next(o)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
    ```

    可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

    回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。

    同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：

    ```python
    >>> for n in fib(3):
    ...     print(n)
    ...
    1
    1
    2
    ```

### 1.2 迭代器

生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器： Iterator 。

|生成器 generator 都是迭代器 Iterator|

可以直接作用于for循环的数据类型有以下几种：

* 一类是集合数据类型，如list、tuple、dict、set、str等； ｜ 不是迭代器，转换方法：使用 iter() 函数将 Iterable 对象 转换为 Iterator
* 一类是generator，包括生成器和带yield的generator function。  ｜ 迭代器
可以直接作用于for循环的对象统称为可迭代对象： Iterable

```python
>>> from collections.abc import Iterable
>>> isinstance([], Iterable)  # 判断是否可迭代
True
>>> isinstance((x for x in range(10)), Iterator)  # 判断是否为迭代器
True
>>> isinstance([], Iterator)
False
>>> isinstance('abc', Iterator)
False
>>> isinstance(iter([]), Iterator)  # iter() 函数将 Iterable 对象 转换为 Iterator
True
>>> isinstance(iter('abc'), Iterator)
True
```

而

## 2 赋值运算法

|运算符|描述|实例|
|-:|-|-|
|=|简单的赋值运算符|c=a+b，将a+b的运算结果赋值为c|
|+=|加法赋值运算符|c+=a <==> c=a+a|
|-=|减法赋值运算符||
|*=|乘法赋值运算符||
|/=|除法赋值运算符||
|%=|取模赋值运算符||
|**=|幂赋值运算符||
|//=|取整除赋值运算符||

## 3 逻辑运算符

|运算符|逻辑表达式|描述|实例|
|-:|-|-|-|
|and|x and y|布尔与 - 如果x为false，x and y返回 false，否则它返回 y 的计算值|-|
|or|x or y|布尔与 - 如果x为非0，它返回x的值，否则返回y的计算值|-|
|not|not x|布尔非|-|

## 4 位运算符

|运算符|描述|实例|
|-:|-|-|
|&|按位与运算符：参与运算的两个值，如果两个相应位都为1，则该位位1，反之为0||
|\||按位或运算符：相应的二进位有一个1，结果位为1||
|^|按位异或运算符：相应的二进位值相异时，结果为1||
|~|按位取反运算符：对每个二进位取反||
|<<|左移运算符：运算符的各二进位均左移若干位，高位丢弃，低位补0| *2|
|>>|右移运算符：运算符的各二进位均右移若干位，高位丢弃，低位补0| /2|

## 5 多进制数

1. 二进制数字由 0 和 1 组成，使用 0b/0B前缀表示

    ```python
    print(int(0b1010))  # 10
    ```

2. 使用 bin() 函数将一个数字转换为它的二进制形式

    ```python
    print(bin(8))  # 0b1000
    ```

3. 八进制由数字 0-7 组成，用前缀 0o/0O 表示八进制

    ```python
    print(oct(8))  # 0o10
    ```

3. 十六进制由数字 0-7 组成，用前缀 0x/0X 表示十六进制

    ```python
    print(hex(8))  # 0x8
    ```

## 6 同步异步阻塞和非阻塞的理解

1. 同步与异步针对的是客户端，同步是指客户端要一直等待服务端返回结果，期间不能做其他事情，异步是指客户端无需等待服务端结果，可以做其他事情
2. 阻塞和非阻塞针对的是服务端，阻塞是指服务端对客户的请求执行系统I/O操作时要等待系统给出结果，期间不能做其他事情，非阻塞是指服务端把请求交给系统I/O后，可以做其他事情，并且会轮询查看之前的请求系统是否给出结果，给出就返回，再处理下一个，没给出就直接处理下一个
3. 同步非阻塞方式在实际中不使用是因为这样客户对会一直需要等待，因为服务端不会专门开一个线程服务该客户端的请求，所以客户端体验是最差的
4. 异步阻塞方式也不在实际中使用是因为客户端可以一直对服务端进行操作，导致服务端压力很大，需要非常多的线程来维护请求，所以这要求服务端的性能非常高才行

select、poll、epoll 模型的区别？

答：select 利用系统自身调度系统，生成一个数组，将监控的文件描述符都放进去，进行遍历监控，文件就绪时传递给程序进行处理。poll 和select 类似，但由于select 类型是数组，存在上限，而 poll 使用链表，没有上限，同时效率比起select 更高。epoll 改进了前两种方式，利用回调函数的方法，将就绪的文件描述符添加进一个数组中，只对这个数组进行遍历

## 7 python 单例模式实现

​单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。

__new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能实例 <这个绝对常考啊.绝对要记住1~2个方法,当时面试官是让手写的。>

1. 使用__new__方法

    ```python
    class Singleton(object):
        def __new__(cls, *args, **kw):
            if not hasattr(cls, '_instance'):
                orig = super(Singleton, cls)
                cls._instance = orig.__new__(cls, *args, **kw)
            return cls._instance

    class MyClass(Singleton):
        a = 1
    ```

2. 共享属性

    创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法

    ```python
    class Borg(object):
        _state = {}
        def __new__(cls, *args, **kw):
            ob = super(Borg, cls).__new__(cls, *args, **kw)
            ob.__dict__ = cls._state
            return ob

    class MyClass2(Borg):
        a = 1
    ```

3. 装饰器版本

    ```python
    def singleton(cls):
        instances = {}
        def getinstance(*args, **kw):
            if cls not in instances:
                instances[cls] = cls(*args, **kw)
            return instances[cls]
        return getinstance

    @singleton
    class MyClass:
    ...
    ```

4. import 方法

    作为 python 的模块是天然的单例模式
    ```python
    # mysingleton.py
    class My_Singleton(object):
        def foo(self):
            pass

    my_singleton = My_Singleton()

    # to use
    from mysingleton import my_singleton

    my_singleton.foo()
    ```