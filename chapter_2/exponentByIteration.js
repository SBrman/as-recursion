function exponentByIteration(a, n) {
    let res = 1;
    for (let i=0; i<n; i++) {
        res *= a;
    }
    return res;
}

document.write(exponentByIteration(3, 6) + "<br />");
document.write(exponentByIteration(10, 3) + "<br />");
document.write(exponentByIteration(17, 10) + "<br />");
</script>
