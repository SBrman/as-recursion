function fib(number) {
	let a = 1, b = 1;
	let tempNum;
	document.write("a = " + a + ", b = " + b + "<br />");
	for (let i=1; i<number; i++) {
		tempNum = a + b;
		a = b;
		b = tempNum;
		document.write("a = " + a + ", b = " + b + "<br />");
	}
	return a;
}


document.write(fib(10));
