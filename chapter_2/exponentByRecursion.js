
function exponentByRecursion(a, n){ 
    if (n == 0) { return 1; }
    if (n == 1) { return a; }
    res = exponentByRecursion(a, Math.floor(n / 2))
    return res * res * exponentByRecursion(a, n % 2)
}

document.write(exponentByRecursion(3, 6) + "<br />");
document.write(exponentByRecursion(10, 3) + "<br />");
document.write(exponentByRecursion(17, 10) + "<br />");

