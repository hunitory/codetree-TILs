const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim())

if ((n % 2 != 0 && n % 3 == 0) ||( n % 2 == 0 && n % 5 == 0) ) {
    console.log("true")
} else {
    console.log("false")
}