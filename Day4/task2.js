let sum = 0;
while (true) {
    let input = prompt("Enter a number (0 to stop):");
    let num = Number(input);

    if (isNaN(num)) {
        alert("Invalid input, please enter a number.");
        continue;
    }
    if (num === 0 || sum + num > 100) {
        if (sum > 0) alert(sum + num);
        else alert(0);
        break;
    }
    sum += num;
}