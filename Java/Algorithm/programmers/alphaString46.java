// [alphaString46.java]
// 문자열 다루기 기본

class Solution {
  public boolean solution(String s) {
      boolean answer = true;
      // 1. 문자열의 길이가 4나 6인지 확인
      if (s.length() == 4 || s.length() == 6) {
        // 2. 각 문자가 숫자인지 확인
        for (int i = 0; i < s.length(); i++) {
          if(Character.isDigit(s.charAt(i))) {
              continue;
          } else {
              answer = false;
              break;
          }
        }
      }
      else {
          answer = false;
      }
      return answer;
    }
}