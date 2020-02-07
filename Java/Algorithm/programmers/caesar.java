// [caesar.java]
// 시저 암호

class Solution {
  public String solution(String s, int n) {
      String answer = "";

      // 1. 한글자씩 반복
      for (int i = 0; i < s.length(); i++) {
          char ch = s.charAt(i);
          
          // 1-1. 공백일 경우
          if (Character.isWhitespace(ch)) {
              answer += " ";
              continue;
          // 1-2. 대문자와 소문자에 따라 아스키코드 계산 후 문자변환
          } else if (Character.isUpperCase(ch)){
              answer += (char)((ch - 'A' + n) % 26 + 'A');
          } else {
              answer += (char)((ch - 'a' + n) % 26 + 'a');
          }
      }
      return answer;
  }
}