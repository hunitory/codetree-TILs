const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim());

let i = 1

while (i <= n) {
    let check_number = i
    check_number = String(check_number);
    let check_num = [...check_number];
    if (i % 3 === 0 || check_num.some(num => ["3", "6", "9"].includes(num))) {
        process.stdout.write(`0 `)
    } else {
        process.stdout.write(`${i} `)
    }

    i++;
}