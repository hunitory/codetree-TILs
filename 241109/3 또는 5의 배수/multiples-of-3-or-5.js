const fs = require("fs");

let a = fs.readFileSync(0).toString().trim()

a = Number(a);

if (a % 3 == 0) {
    console.log("YES")
} else {
    console.log("NO")
}

if (a % 5 == 0) {
    console.log("YES")
} else {
    console.log("NO")
}