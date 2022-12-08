const express = require('express');
const sqlite3 = require('sqlite3');
const cors = require('cors')


const app = express();
app.use(cors())
// Connecting Database
let db = new sqlite3.Database('./db/sample.db');

//db.run("CREATE TABLE adam (first_name TEXT NOT NULL, last_name TEXT NOT NULL)")


app.get('/', (req, res) => {
    
    res.send("aaaaaa");
})

app.get('/get', (req, res) => {
    let sql = `SELECT * FROM adam`

    db.all(sql, [], (err, rows) => {
        if (err) {
            throw err;
        }
        console.log('sending' + rows)
        res.status(200).json(rows)
    });
})

app.get('/add', (req, res) => {
    db.run("INSERT INTO adam(first_name, last_name)VALUES('AAA', 'BBBB');")
    res.send()
})

app.listen(4000, () => {
    console.log("server started");
})