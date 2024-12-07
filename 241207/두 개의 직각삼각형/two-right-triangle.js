const fs = require("fs");

const n = Number(fs.readFileSync(0).toString().trim())

let str = "";

for ( let i = 0; i < n; i++ ) {
    str = "";
    for ( let j = 0; j + i< n; j++ ) {
        str += "*";
    }

    for ( let jj = n; jj - i < n; jj++ ) {
        str += " "
    }

    for ( let kk = n; kk - i < n; kk++ ) {
        str += " "
    }


    for ( let k = 0; k + i< n; k++ ) {
        str += "*";
    }
    console.log(str)
}