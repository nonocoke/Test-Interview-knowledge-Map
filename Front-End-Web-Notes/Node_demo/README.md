# Node-demo-class

* [link: blog-1](./blog-1)
* [link: blog-express](./blog-express)
* [link: blog-koa2](./blog-koa2)

## blog-1

### blog-1 不使用框架开发 server 的总结

* 开放了哪些功能模块、完整的流程
* 用到了哪些核心的知识点
* 回顾 "server 和 前端的区别"

### 功能模块

1. 处理 http 接口
2. 连接数据库
3. 实现登录
4. 日志
5. 安全
6. 上线（--）

### 核心知识点

* http, nodejs 处理 http, 处理路由, mysql
* cookie, session, redis, nginx 反向代理
* sql 注入, xss 攻击, 加密
* 日志, stream, crontab, readline
* (线上)

### server 和前端的区别

* 服务稳定性（--）
* 内存 CPU（优化 扩展）[stream, session-redis]
* 日志记录
* 安全（含 登录验证）
* 集群和服务拆分（设计已支持）

### Web 安全

* sql 注入：窃取数据库内容
* xss 攻击：窃取前端的 cookie 内容
* 密码加密： 保障用户信息安全

```text
sql 注入：
1. 最原始、最简单的攻击，从有了web2.0就有了 sql 注入攻击
2. 攻击方式： 输入一个 sql 片段，最终拼接成一段攻击代码
3. 预防措施： 使用mysql.escape 函数处理输入内容即可（特殊字符转义）

xss 攻击：
1. 前端同学最熟悉的攻击方式，但 server 端更应该掌握
2. 攻击方式：在页面展示内容中掺杂 js 代码，以获取网页信息
3. 预防措施：转换生成 js 的特殊字符
(
&. -> &amp;
<  -> &lt;
>  -> &gt;
"  -> &quot;
'  -> &#x27;
/. -> &#x2F;
)
<script>alert(document.cookie)</script>

密码加密：
1. 万一数据库被用户攻破，最不应该泄漏的就是用户信息
2. 攻击方式：获取用户名和密码，再去尝试登录其它系统
3. 预防措施：将密码加密，即便拿到密码也不知道明文
```

### http-server

nginx 反向代理：

```bash
sudo vim /usr/local/etc/nginx/nginx.conf
# > [update location]
server {
        listen       8080;
        server_name  localhost;

        #location / {
        #    root   html;
        #    index  index.html index.htm;
        #}

        location / {
                proxy_pass http://localhost:8001;
        }
        location /api/ {
                proxy_pass http://localhost:8000;
                proxy_set_header Host $host;
```

html 服务
http-server -p 8001

## blog-express

### Express

### Pre

1. nginx 代理
2. redis-server 启动 redis 服务
3. npm run dev 启动后端服务
4. http-server -p 8001 启动前端服务

### Express 安装与使用

* 安装（脚手架 express-generator）
    1. npm install express-generator -g
    2. express express-test
    3. npm install & npm start
* 初始化代码介绍、处理路由
* 使用中间件

### Changes

* 使用 express-session, connect-redis, loginCheck 中间件
* morgan 日志插件
* express 使用及原理

## blog-koa2

### koa2

* express 中间件是异步回调，koa2 原生支持 async/await
* 新开发框架和系统，都开始基于 koa2，例如 egg.js

```text
async await 要点：
1. await 后面可以追加 promise 对象，获取 resolve 的值
2. await 必须包裹在 async 函数里面
3. async 函数执行返回的也是一个 promise 对象
4. try-catch 截获 promise 中 reject 的值
```

安装 koa2

* npm install koa-generator -g
* Koa2 koa2-test
* npm install & npm run dev

### 实现登录

* 和 express 类似
* 安装插件 npm i koa-generic-session koa-redis redis --save
* 安装插件 npm i mysql xss --save

### 日志

* access log 记录，使用 morgan
* 自定义日志使用 console.log 和 console.error

### 线上环境

PM2 解决以下问题：

* 服务器稳定性
* 充分利用服务器硬件资源，以便提高性能
* 线上日志记录

PM2 功能>

1. 进程守护
2. 启动多进程，充分利用 CPU 和内存
3. 自带日志记录功能

PM2 流程

1. 介绍 (后台运行)
    * 安装 npm i pm2 -g
    * 命令：
        1. pm2 start ..., pm2 list
        2. pm2 restart \<name\>/\<id\>, pm2 start \<name\>/\<id\>, pm2 stop \<name\>/\<id\>
        3. pm2 info \<name\>/\<id\>, pm2 log \<name\>/\<id\>, pm2 monit \<name\>/\<id\>
2. 进程守护
3. 配置和日志记录
4. 多进程
5. 关于服务器运维
