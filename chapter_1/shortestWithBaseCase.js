function shortestWithBaseCase(makeRecursiveCall) {
	document.write("shortestWithBaseCase(" + makeRecursiveCall + ") called.<br />");
	if (makeRecursiveCall === false) {
		document.write("Returning from base case.<br />");
		return;
	} else {
		shortestWithBaseCase(false);
		document.write("Returning from Recursive case.<br />");
		return;
	}

}


document.write("Calling shortestWithBaseCase(false):<br />");
shortestWithBaseCase(false);
document.write("<br />");

document.write("Calling shortestWithBaseCase(true):<br />");
shortestWithBaseCase(true);
