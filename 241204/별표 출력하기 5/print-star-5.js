const fs = require("fs");

const n = Number(fs.readFileSync(0).toString().trim());

let str = "";

for (let i = 0; i < n; i++) {
    str = ""
    for (let j = 0; j < n - i; j++) {
        for (let k = 0; k < n - i; k++ ) {
            str += '*';
        }
        str += ' ';
    }
    console.log(str)
}