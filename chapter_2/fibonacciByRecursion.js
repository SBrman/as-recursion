function fib(n) {
	document.write("Called fib(" + n + ")<br />");
	if (n==0 || n == 1) {
		document.write("Returning 1.<br />");
		return 1;
	} else {
		document.write("Calling fib(" + (n-1) + ") " + "and fib(" + (n-2) + ")<br />");
		let res = fib(n-1) + fib(n-2);
		document.write("Call to fib("+ n +") Returning " + res + "<br />");
		return res;
	}
}
document.write(fib(5));
