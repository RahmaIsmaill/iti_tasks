  function findLetterPositions() {
      let sentence = prompt("Enter a sentence:");
      let letter = prompt("Enter a letter to search for:");
      let positions = [];

      for (let i = 0; i < sentence.length; i++) {
        if (sentence[i] === letter) {
          positions.push(i);
        }
      }

      alert("Positions: [" + positions.join(", ") + "]");
    }

    findLetterPositions();