const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let m;

rl.on("line" , (input) => {
    m = Number(input.trim())
    if (3 <= m && m <= 5) {
        console.log("Spring");
    } else if (6 <= m && m <= 8) {
        console.log("Summer");
    } else if (9 <= m && m <= 11) {
        console.log("Fall");    
    } else {
        console.log("Winter");
    }

    rl.close()
})