
    function counte() {
      let str = prompt("Enter a string:");
      let count = 0;
      for (let i = 0; i < str.length; i++) {
        if (str[i] === 'e') {  // ||str[i] === 'E'
          count++;
        }
      }
      alert("The number of 'e' characters: " + count);
    }

    counte();
