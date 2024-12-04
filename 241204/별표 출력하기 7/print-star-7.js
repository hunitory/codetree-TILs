const fs = require("fs");

const n = Number(fs.readFileSync(0).toString().trim())

let str = "";

for ( let i = 0; i < n; i++ ) {
    str = ""
    for (let j = 0; j <= i; j++) {
        str += '* '
    }
    console.log(str)
}