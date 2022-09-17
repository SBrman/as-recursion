function a() {
	document.write("a is called.<br />");
	b();
	document.write("a is returning.<br />");
}
function b() {
	document.write("b is called.<br />");
	c();
	document.write("b is returning.<br />");
}
function c() {
	document.write("c is called.<br />");
	document.write("c is returning.<br />");
}

