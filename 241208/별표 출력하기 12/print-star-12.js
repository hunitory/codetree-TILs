const fs = require("fs");
const n = Number(fs.readFileSync(0).toString().trim());

let str = "";

for ( let i = 0; i < n; i++ ) {
    str = "";
    for ( let j = 0; j < n; j++ ) {
        if ( i <= j && j % 2 != 0) {
            str += "* "
        } else {
            if ( i === 0 ) {
                str += "* "
            } else {
                str += "  "
            }
        }
    }
    console.log(str)
}