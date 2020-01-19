(function a(a) {
  const array = [...a];

  let vogais = [];
  let consoantes = [];

  for (let i = 0; i < array.length; i++) {
    if (vogal(array[i])) {
      vogais.push(array[i]);
    } else {
      consoantes.push(array[i]);
    }
  }

  console.log(sort(vogais), consoantes);
})("birola");

function sort(array) {
  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      let aux;
      if (array[i] > array[j]) {
        aux = array[j];
        array[j] = array[i];
        array[i] = aux;
      }
    }
  }

  return array;
}

function vogal(p) {
  const letra = p.toLowerCase();

  return (
    letra === "a" ||
    letra === "e" ||
    letra === "i" ||
    letra === "o" ||
    letra === "u"
  );
}
