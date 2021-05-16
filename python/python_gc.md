# Python 垃圾回收机制

整数

* 小整数：Python 对小整数的定义是 __[-5, 127]__ 这些整数对象是提前建立好的，不会被垃圾回收。在一个 Python 程序中，所有位于这个范围内使用的都是同一个对象。__单个字母__ 同样也是如此。
* 大整数：每一个大整数的创建均在内存中会分配一个内存空间，所以大整数的内存空间是需要被回收的

Gc： 引用计数为主，标记清除和分代回收为辅

引用计数
引用计数法机制的原理是：每个对象维护一个ob_ref字段，用来记录该对象当前被引用的次数，每当新的引用指向该对象时，它的引用计数ob_ref加1，每当该对象的引用失效时计数ob_ref减1，一旦对象的引用计数为0，该对象立即被回收，对象占用的内存空间将被释放。
优点：
1、简单
2、实时性：一旦没有引用，内存就直接释放了，不用像其他机制得等到特定时机。实时性还带来一个好处：处理回收内存的时间分摊到了平时。
缺点：
1、维护引用计数消耗资源
2、循环引用

标记清除 (三色标记法)
标记清除（Mark—Sweep）』算法是一种基于追踪回收（tracing GC）技术实现的垃圾回收算法。它分为两个阶段：第一阶段是标记阶段，GC会把所有的『活动对象』打上标记，第二阶段是把那些没有标记的对象『非活动对象』进行回收。那么GC又是如何判断哪些是活动对象哪些是非活动对象的呢？
对象之间通过引用（指针）连在一起，构成一个有向图，对象构成这个有向图的节点，而引用关系构成这个有向图的边。从根对象（root object）出发，沿着有向边遍历对象，可达的（reachable）对象标记为活动对象，不可达的对象就是要被清除的非活动对象。根对象就是全局变量、调用栈、寄存器。 mark-sweepg 在上图中，我们把小黑圈视为全局变量，也就是把它作为root object，从小黑圈出发，对象1可直达，那么它将被标记，对象2、3可间接到达也会被标记，而4和5不可达，那么1、2、3就是活动对象，4和5是非活动对象会被GC回收。
标记清除算法作为Python的辅助垃圾收集技术主要处理的是一些容器对象，比如list、dict、tuple，instance等，因为对于字符串、数值对象是不可能造成循环引用问题。Python使用一个双向链表将这些容器对象组织起来。

分代回收
分代回收是一种以空间换时间的操作方式，Python将内存根据对象的存活时间划分为不同的集合，每个集合称为一个代，Python将内存分为了3“代”，分别为年轻代（第0代）、中年代（第1代）、老年代（第2代），他们对应的是3个链表，它们的垃圾收集频率随着对象存活时间的增大而减小。
新创建的对象都会分配在年轻代，年轻代链表的总数达到上限时，Python垃圾收集机制就会被触发，把那些可以被回收的对象回收掉，而那些不会回收的对象就会被移到中年代去，依此类推，老年代中的对象是存活时间最久的对象，甚至是存活于整个系统的生命周期内。
同时，分代回收是建立在标记清除技术基础之上。分代回收同样作为Python的辅助垃圾收集技术处理那些容器对象

垃圾回收
有三种情况会触发垃圾回收：
调用gc.collect(),需要先导入gc模块。
当gc模块的计数器达到阈值的时候。
程序退出的时候。