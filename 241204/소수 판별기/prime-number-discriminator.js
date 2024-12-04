const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim())

let flag = true;

for ( let i = 2; i <= Math.sqrt(n); i ++ ) {
    if ( n % i === 0 ) {
        flag = false;
        break
    } 
}

if (flag) {
    console.log("P")
} else {
    console.log("C")
}