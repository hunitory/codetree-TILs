const readline = require("readline");
const { stdin : input, stdout : output } = require("process");
const rl = readline.createInterface({ input , output });

let a;

rl.on("line", (input) => {
    a = Number(input.trim());
    if (a === 1) {
        console.log("John")
    } else if (a === 2) {
        console.log("Tom");
    } else if (a === 3) {
        console.log("Paul");
    } else if (a === 4) {
        console.log("Sam");
    } else {
        console.log("Vacancy")
        rl.close();
    }
})

rl.on("close", () => {
    process.exit(0); // 프로세스 종료
});