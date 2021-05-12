# koa2

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

## 实现登录

* 和 express 类似
* 安装插件 npm i koa-generic-session koa-redis redis --save
* 安装插件 npm i mysql xss --save

## 日志

* access log 记录，使用 morgan
* 自定义日志使用 console.log 和 console.error

## 线上环境

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
        2. pm2 restart <name>/<id>, pm2 start <name>/<id>, pm2 stop <name>/<id>
        3. pm2 info <name>/<id>, pm2 log <name>/<id>, pm2 monit <name>/<id>
2. 进程守护
3. 配置和日志记录
4. 多进程
5. 关于服务器运维
