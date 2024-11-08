const readline = require("readline");

const rl = readline.createInterface({
    input = process.stdin,
    output = process.stdout
});

let s;

rl.on("line", (input) => {
    s = input
}).on("close", () => {
    if ( s === "S") {
        console.log("Superior");
    } else if ( s === "A") {
        console.log("Excellent");
    } else if ( s === "B") {
        console.log("Good");
    } else if ( s === "C") {
        console.log("Usually");
    } else if ( s === "D") {
        console.log("Effort");
    } else {
        console.log("Failuire")
    }
})