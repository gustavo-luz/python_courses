const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function countLastZeros(num) {
  var zeros = 0;
  var count = 0;

  for (var i in num) {
    if (num[i] === "0") {
        do {
          count++;
          zeros++;
          console.log(zeros);
        } while(i + count < num.length && num[i + count + 1] === "0");
        return zeros;
    }
  }
}

rl.question('', (num) => {

    num = num.split("").reverse();
    var zeros = countLastZeros(num);

    rl.close();
});