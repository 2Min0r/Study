// [toWeridCase.java]
// 이상한 문자 만들기

class Solution {
  public String solution(String s) {
      String answer = "";
      String[] div = s.split(" ", -1);
      for (int i=0; i < div.length; i++){
          for (int j=0; j < div[i].length(); j++){
              if ((j+1) % 2 != 0) {
                  answer += Character.toUpperCase(div[i].charAt(j));
              } else {
                  answer += Character.toLowerCase(div[i].charAt(j));
              }
          }
          if (i != div.length-1)
              answer += " ";
      }
      return answer;
  }
}