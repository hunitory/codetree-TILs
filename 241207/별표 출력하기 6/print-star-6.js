const fs = require("fs");
const n = Number(fs.readFileSync(0).toString().trim());

let str = "";

for ( let i = 0; i < n; i++ ) {
    str = "";
    for ( let j = n ; j - i < n; j++ ) {
        str += "  "
    }

    for ( let j = 1; j < (n * 2) - (i * 2); j++ ) {
        str += "* "
    }
    console.log(str);
}

for ( let i = 1; i < n; i++ ) {
    str = "";
    for ( let j = 1; j + i < n; j++ ) {
        str += "  ";
    }

    for ( let j = n; (j * 2) - 2 * (i * 2) <= n * 2 ; j++ ) {
        str += "* ";
    }
    console.log(str);
}