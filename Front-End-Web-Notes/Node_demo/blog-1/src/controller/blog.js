const xss = require('xss')
const { exec } = require('../db/mysql')

const getList = (author, keyword) => {
    // where `1=1` => 防止 author, keyword 都为空
    let sql = `select * from blogs where 1=1 `
    if (author) {
        sql += `and author='${author}' `
    }
    if (keyword) {
        sql += `and title like '%${keyword}%' `
    }
    sql += `order by createtime desc;`

    // 返回 promise
    return exec(sql)
}

const getDetail = (id) => {
    const sql = `select * from blogs where id=${id}`
    return exec(sql).then(rows => {
        return rows[0]
    })
}

const newBlog = (blogData = {}) => {
    // blogData is a object of blog, include title, content, author...
    const title = xss(blogData.title)
    const content = xss(blogData.content)
    const author = blogData.author
    const createtime = Date.now()

    const sql = `
        insert into blogs(title, content, createtime, author) 
        values ('${title}','${content}', ${createtime},'${author}');
    `
    return exec(sql).then(insertData => {
        // console.log('insertData> ', insertData)
        return {
            id: insertData.insertId
        }
    })
}

const updateBlog = (id, blogData = {}) => {
    const title = xss(blogData.title)
    const content = xss(blogData.content)
    const sql = `
        update blogs set title = '${title}', content = '${content}' where id = ${id};
    `
    return exec(sql).then(updateData => {
        // console.log('updateData> ', updateData)
        if (updateData.affectedRows > 0) {
            return true
        }
        return false
    })
}

const delBlog = (id, author) => {
    const sql = `
        delete from blogs where id = '${id}' and author = '${author}'
    `
    return exec(sql).then(delData => {
        console.log('delData >\n', delData)
        if (delData.affectedRows === 1) {
            return true
        }
        return false
    })
}

module.exports = {
    getList,
    getDetail,
    newBlog,
    updateBlog,
    delBlog
}
