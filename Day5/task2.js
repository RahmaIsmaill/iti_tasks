   function checkPalindrome() {

      let str = prompt("Enter a string:");
      let caseSensitive = confirm("Do you want to consider case sensitivity?");

      let original = caseSensitive ? str : str.toLowerCase(); //itI //iti
      let reversed = original.split("").reverse().join(""); //Iti   //iti

      if (original === reversed) {
        alert("The string is a palindrome.");
      } else {
        alert("The string is NOT a palindrome.");
      }
    }

    checkPalindrome();