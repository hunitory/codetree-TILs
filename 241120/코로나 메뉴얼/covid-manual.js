const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({
    input,
    output
})

let cnt = 0;

rl.on("line", (input) => {
    let person = input.trim().split(" ")
    let cold = person[0]
    let tem = Number(person[1])

    if ( cold === "Y") {
        if ( tem >= 37 ){
            cnt += 1
        }
    }

}).on("close", () => {
    if ( cnt >= 2) {
        console.log("E")
    } else {
        console.log("N")
    }
})