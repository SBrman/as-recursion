let NUMBER = 5;

document.write("Code in a loop:<br />")
let i = 0;
while (i < NUMBER) {
	document.write(i++ + ", Hello world.<br />");
}

document.write("Code in a loop:<br />")
function hello(i) {
	if (i === undefined) {
		i = 0;
	}
	document.write(i++ + ", Hello world.<br />");
	if (i >= NUMBER) {
		return;
	} else {
		hello(i);
	}
}
hello();
