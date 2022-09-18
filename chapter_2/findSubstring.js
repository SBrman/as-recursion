function findSubstringIterative(substring, string){
	let i = 0;
	while (i < string.length) {
		if (string.substring(i, i+substring.length) == substring) {
            return i;
        }
        i++;
	}
    return -1;
}

function findSubstringRecursive(substring, string, i){
    if (i === undefined) {i = 0;}
    document.write(i);
    if (i >= string.length){
        return -1;
    }
    if (string.substring(i, i+substring.length) == substring) {
        return i;
    } else {
        return findSubstringRecursive(substring, string, ++i);
    }
}

document.write(findSubstringIterative('substring', 'Find the index of the substring in this sentence.') + "<br />");
document.write(findSubstringRecursive('substring', 'Find the index of the substring in this sentence.') + "<br />");
