const { login } = require('../controller/user')
const { SuccessModel, ErrorModel} = require('../model/resModel')
const { set } = require('../db/redis')

const handleUserRouter = (req, res) => {
    const method = req.method

    // login
    if (method === 'POST' && req.path === '/api/user/login') {
        // console.log('...', req.body)
        const { username, password } = req.body
        const result = login(username, password)
        return result.then(data => {
            if (data.username) {
                // 设置 session
                req.session.username = data.username
                req.session.realname = data.realname
                // 同步到 redis
                set(req.sessionId, req.session)

                return new SuccessModel()
            }
            return new ErrorModel('login check error.')
        })
    }

    // if (method === 'GET' && req.path === '/api/user/login-test') {
    //     if (req.session.username) {
    //         return Promise.resolve(new SuccessModel({session: req.session}))
    //     }
    //     return Promise.resolve(new ErrorModel('login-test error.'))
    // }
}

module.exports = handleUserRouter
