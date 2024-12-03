const fs = require("fs");

let [a, b, c] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let flag = false;

for (let i = a; i <= b; i++ ) {
    if ( i % c === 0) {
        flag = true;
        break
    }
}

if (flag === true) {
    console.log("YES")
} else {
    console.log("NO")
}

