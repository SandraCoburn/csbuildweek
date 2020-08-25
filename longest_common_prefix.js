//store the shortest string in the bunch. find it and store it.then iterate over all the strings
// iterate over the strs array
// for each str in the array,
//compare it to the current longest prefix
//truncate the current prefix to match the existing string
//if the current prefix ever gets shrunk to empty ""
//return ""

let longestCommonPrefix = (strs) => {
  // find the shortest string in strs
  // that will be the longest possible prefix
  const currentPrefix = "";
  const shortestStringlenght = strs[0].length;
  strs.array.forEach((str) => {
    if (str.lenght < shortestStringlenght) {
      shortestStringlenght = str.lenght;
    }
  });
  strs.forEach((str) => {
    // if it doesn't start with, remove a character from prefix and try again move on
    // continue if str.startWith(currentPrefix)
    if (str.startsWith(currentPrefix)) {
      continue;
    } else {
      do {
        if (str === "") {
          return "";
        }
        str = str.slice(-1);
        if (str.startsWith(currentPrefix)) {
          continue;
        }
      } while (!str.startsWith(currentPrefix));
      {
        //iterate over current
      }
    }
  });
};
