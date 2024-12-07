const fs = require("fs");
const n = Number(fs.readFileSync(0).toString().trim());

let str = "";

const dis = (2 * n) + 1

for ( let i = 0; i < dis; i++ ) {
    str = "";
    for (let j = 0; j < dis; j++ ) {
        if ( i % 2 === 1 && j % 2 === 1 ) {
            str += "  "
        } else {
            str += "* "
        }
    }
    console.log(str)
}