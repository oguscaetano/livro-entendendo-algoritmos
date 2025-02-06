const quickSort = (array) => {
  if (array.length <= 1) {
    return array;
  }

  let pivot = array[0];
  let menores = [];
  let maiores = [];

  for (let index = 1; index < array.length; index += 1) {
    if (array[index] < pivot) {
      menores.push(array[index]);
    } else {
      maiores.push(array[index]);
    }
  }

  return [...quickSort(menores), pivot, ...quickSort(maiores)];
};