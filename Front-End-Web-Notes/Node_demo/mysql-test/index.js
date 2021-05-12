const mysql = require('mysql')

const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    port: '3306',
    database: 'myblog'
})

conn.connect()

const sql = `insert into blogs (title, content, createtime, author) values ('标题C', '内容C', 1546871704408, 'zhangsan')`
conn.query(sql, (err, result) => {
    if (err) {
        console.error(err)
        return
    }
    console.log(result)
})

conn.end()
