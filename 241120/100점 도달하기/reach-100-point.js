const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim());

for (let i = 0; i + n <= 100 ; i ++) {
    if ((i + n) >= 90) {
        process.stdout.write("A" + " ");
    } else if ((i + n) >= 80) {
        process.stdout.write("B" + " ");
    } else if ((i + n) >= 70) {
        process.stdout.write("C" + " ");
    } else if ((i + n) >= 60) {
        process.stdout.write("D" + " ");
    } else {
        process.stdout.write("F" + " ");
    }
}