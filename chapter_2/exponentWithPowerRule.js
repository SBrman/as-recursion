function exponentWithPowerRule(a, n) {
    let operationStack = [];
    while (n > 1) {
        if (n % 2 == 0) {
            operationStack.push("square");
            n = Math.floor(n / 2);
        } else {
            operationStack.push("multiply");
            n--;
        }
    }

    let result = a;
    while (operationStack.length > 0) {
        let operation = operationStack.pop();
        if (operation === "multiply") {
            result *= a;
        } else if (operation === "square") {
            result *= result;
        }
    }

    return result;
}


document.write(exponentWithPowerRule(3, 6) + "<br />");
document.write(exponentWithPowerRule(10, 3) + "<br />");
document.write(exponentWithPowerRule(17, 10) + "<br />");

