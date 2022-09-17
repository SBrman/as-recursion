
function a() {
	let spam = "Ant";
	document.write("a: Spam is " + spam + "<br />");
	b();
	document.write("a: Spam is " + spam + "<br />");
}


function b() {
	let spam = "Bobcat";
	document.write("b: Spam is " + spam + "<br />");
	c();
	document.write("b: Spam is " + spam + "<br />");
}

function c() {
	let spam = "Coyote";
	document.write("c: Spam is " + spam + "<br />");
}

a()

