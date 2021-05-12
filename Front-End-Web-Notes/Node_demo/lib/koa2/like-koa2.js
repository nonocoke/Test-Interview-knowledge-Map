const http = require('http')

// 组合中间件
function compose(middlewareList) {
    return function (ctx) {
        function dispatch(i) {
            const fn = middlewareList[i]
            try {
                // 兼容两种格式中间件， 均返回一个 Promise 对象
                //   1. app.use(async (ctx, next) => {})
                //   2. app.use((ctx, next) => {})
                return Promise.resolve(
                    fn(ctx, dispatch.bind(null, i + 1))  // promise
                )
            } catch (err) {
                return Promise.reject(err)
            }
        }
        return dispatch(0)
    }
}

class LikeKoa2 {
    /* koa2 中间件:
        1. app.use 用来注册中间件，先收集起来
        2. 实现 next 机制，即上一个通过 next 触发下一个
        3. （不涉及 method 和 path 的判断）
    */
    constructor() {
        this.middlewareList = []
    }

    use(fn) {
        this.middlewareList.push(fn)
        return this
    }

    createContext(req, res) {
        const ctx = {
            req,
            res
        }
        ctx.query = req.query  // ...
        return ctx
    }

    handleRequest(ctx, fn) {
        return fn(ctx)
    }

    callback() {
        const fn = compose(this.middlewareList)

        return (req, res) => {
            const ctx = this.createContext(req, res)
            return this.handleRequest(ctx, fn)
        }
    }

    listen(...args) {
        const server = http.createServer(this.callback())
        server.listen(...args)
    }
}

module.exports = LikeKoa2
