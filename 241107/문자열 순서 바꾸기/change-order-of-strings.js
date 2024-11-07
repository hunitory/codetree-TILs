const fs = require("fs");

let inputs = fs.readFileSync(0).toString().trim().split("\n");

let s_list = [inputs[0], inputs[1]];

[s_list[0], s_list[1]] = [s_list[1], s_list[0]];

s_list.forEach(s => {
    console.log(s);
});