// class Solution:
//     def isValid(self, s: str) -> bool:
//         ref = {'(' : ')', "[":']', '{':'}'}
//         stack = []
//         lst = list(s)
//         for char in s:
//             if char in ref:
//                 stack.append(ref[char])
//             else:
//                 if not stack:
//                     return False
//                 op = stack.pop()
//                 if char != op:
//                     return False
//         if len(stack):
//             return False
//         return True

let isValid = (str) => {
  // count the number of open parens, curlies, and
  // use a stack
  // push the opener onto the stack as I move left to right
  // pop off the stack and make sure it matches as I'm popping it off
  // if it doesn't match , return invalid
  // when the string is complete, if the stack isn't
};
