const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let a, b;

function check_even (num) {
    return num % 2 === 0
}

rl.on("line" , (input) => {
    [a, b] = input.trim().split(" ").map(Number)
}).on("close", () => {
    if (check_even(a)) {
        console.log("even")
    } else {
        console.log('odd')
    }

    if (check_even(b)) {
        console.log("even")
    } else {
        console.log('odd')
    }
})