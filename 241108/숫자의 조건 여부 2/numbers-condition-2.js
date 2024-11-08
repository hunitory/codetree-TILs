const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let a;

rl.on("line", (input) => { 
    a = Number(input)
}).on("close", () => {
    if (a === 5) {
        console.log("A");
    }
    
    if (a % 2 === 0) {
        console.log("B");
    }
})