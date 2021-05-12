const { genPassword } = require('../utils/cryp')
const { exec, escape } = require('../db/mysql')

const login = async (username, password) => {
    username = escape(username)
    // lock-password-md5
    password = genPassword(password)
    password = escape(password)

    // console.log(username, password)
    const sql = `
        select username, realname from users where username = ${username} and password = ${password}
    `

    const rows = await exec(sql)
    return rows[0] || {}
    // console.log(sql)
    // return exec(sql).then(rows => {
    //     return rows[0] || {}
    // })
}

module.exports = {
    login
}