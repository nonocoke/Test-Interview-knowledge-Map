const http = require('http')
const slice = Array.prototype.slice

class LikeExpress {
    /* express 中间件:
        1. app.use 用来注册中间件，先收集起来
        2. 遇到 http 请求，根据 path 和 method 判断触发哪些
        3. 实现 next 机制，即上一个通过 next 触发下一个
    */
    constructor() {
        // 存放中间件的列表
        this.routes = {
            all: [],  // app.use(...)
            get: [],  // app.get(...)
            post: []  // app.post(...)
        }
    }

    register(path) {
        const info = {}
        // 第一个参数为显示路由
        if (typeof path === 'string') {
            info.path = path
            // 从第二个参数开始，转换为数组，存入 stack
            info.stack = slice.call(arguments, 1)
        } else {
            info.path = '/'
            // 从第一个参数开始，转换为数组，存入 stack
            info.stack = slice.call(arguments, 0)
        }
        return info
    }

    use() {
        const info = this.register.apply(this, arguments)
        this.routes.all.push(info)
    }

    get() {
        const info = this.register.apply(this, arguments)
        this.routes.get.push(info)
    }

    post() {
        const info = this.register.apply(this, arguments)
        this.routes.post.push(info)
    }

    match(method, url) {
        let stack = []
        if (url === '/favicon.ico') {
            return stack
        }

        // 获取 routes
        let curRoutes = []
        curRoutes = curRoutes.concat(this.routes.all)
        curRoutes = curRoutes.concat(this.routes[method])

        curRoutes.forEach(routeInfo => {
            if (url.indexOf(routeInfo.path) === 0) {
                // url = 'api/get-cookie' && routeInf'o.path === '/'
                // url = 'api/get-cookie' && routeInf'o.path === '/api'
                // url = 'api/get-cookie' && routeInf'o.path === '/api/cookie'
                stack = stack.concat(routeInfo.stack)
            }
        })
        return stack
    }

    // 核心 next 机制
    handle(req, res, stack) {
        const next = () => {
            // 拿到第一个匹配的中间件
            const middleware = stack.shift()
            if (middleware) {
                // exec 中间件函数
                middleware(req, res, next)
            }
        }
        next()
    }

    callback() {
        return (req, res) => {
            res.json = (data) => {
                res.setHeader('Content-type', 'application/json')
                res.end(
                    JSON.stringify(data)
                )
            }

            const url = req.url
            const method = req.method.toLowerCase()

            const resultList = this.match(method, url)
            // 
            this.handle(req, res, resultList)
        }
    }

    listen(...args) {
        const server = http.createServer(this.callback())
        server.listen(...args)
    }
}

// 工厂函数
module.exports = () => {
    return new LikeExpress()
}
