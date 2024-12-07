const fs = require("fs");
const n = Number(fs.readFileSync(0).toString().trim());

let str = "";

for ( let i = 0; i < n * 2; i++ ) {
    str = "";
    if ( i % 2 === 0) { 
        for (let j = 0; j + parseInt(i / 2)< n; j++) {
            str += "* ";
        }
    } else {
        for (let j = n; j - parseInt((i - 1) / 2) <= n; j++) {
            str += "* ";
        }
    }
    console.log(str);
}