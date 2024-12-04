const fs = require("fs");

const n = Number(fs.readFileSync(0).toString().trim());

let str = "";
let cnt = 0;

for (let i = 0; i < n; i++ ) {
    str = "";
    for (let j = 0; j < n - cnt; j++) {
        str += "* "
    }
    console.log(str);
    cnt++;
}