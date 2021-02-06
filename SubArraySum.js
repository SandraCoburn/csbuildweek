function subarrayOfGivenSum(positiveIntegerArray, targetSum) {
  let [n, partialSum, j] = [posiriveIntegerArray.length, 0, 0];
  for (let i = 0; i < n; i++) {
    for (; j < n && partialSum + positiveIntegerArray[j] <= targetSum; j++) {
      partialSum += positiveIntegerArray[j];
      if (partialSum == targetSum) {
        return [i, j];
      }
    }
    partialSum -= positiveIntegerArray[i];
  }
}
