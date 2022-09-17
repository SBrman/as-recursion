let callStack = [];
let currentDict = {"returnAddress": "start", "number": 5};
callStack.push(currentDict);
let returnValue;

while (callStack.length > 0) {
let number = callStack[callStack.length - 1]["number"]
let returnAddress = callStack[callStack.length - 1]["returnAddress"]

if (returnAddress === 'start') {
    if (number === 1) {
	returnValue = 1;
	callStack.pop();
	continue;
    } else {
	callStack[callStack.length - 1]["returnAddress"] = "after recursive call";
	currentDict = {"returnAddress": "start", "number": number - 1};
	callStack.push(currentDict);
    }
} else if (returnAddress === "after recursive call") {
    returnValue = returnValue * number;
    callStack.pop();
    continue;
}
}
document.write(returnValue + "<br />");
