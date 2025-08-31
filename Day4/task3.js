 let num = prompt("Enter a number:");
    num = Number(num);

    if (isNaN(num)) {
      document.write("Please enter a valid number!");
    } else {
      if (num % 3 === 0 && num % 5 === 0) {
        document.write(num + " is divisible by both 3 and 5.");
      } else if (num % 3 === 0) {
        document.write(num + " is divisible by 3 only.");
      } else if (num % 5 === 0) {
        document.write(num + " is divisible by 5 only.");
      } else {
        document.write(num + " is not divisible by 3 or 5.");
      }
    }