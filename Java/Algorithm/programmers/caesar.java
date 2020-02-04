// [caesar.java]
// 시저 암호

class Solution {
  public String solution(String s, int n) {
      String answer = "";
      for (int i = 0; i < s.length(); i++) {
          char ch = s.charAt(i);
          if (Character.isWhitespace(ch)) {
              answer += " ";
              continue;
          } else if (Character.isUpperCase(ch)){
              answer += (char)((ch - 'A' + n) % 26 + 'A');
          } else {
              answer += (char)((ch - 'a' + n) % 26 + 'a');
          }
      }
      return answer;
  }
}