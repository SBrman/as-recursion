
function factorial(number) {
	let product = 1;
	for (let i=1; i<=number; i++) {
		product *= i;
	}
	return product;
}

document.write(factorial(5) + "<br />")
