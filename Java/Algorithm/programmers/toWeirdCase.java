// [toWeridCase.java]
// 이상한 문자 만들기

class Solution {
  public String solution(String s) {
      String answer = "";
      // 1. 문자를 " "으로 분리하여 배열에 저장한다.
      String[] div = s.split(" ", -1);
      // 2. 각 문자별로 이므로 따로 반복문을 돌리며,
      for (int i=0; i < div.length; i++){
          for (int j=0; j < div[i].length(); j++){
              // 3. 배열의 위치에 따라 대문자/소문자를 구별한다.
              if ((j+1) % 2 != 0) {
                  answer += Character.toUpperCase(div[i].charAt(j));
              } else {
                  answer += Character.toLowerCase(div[i].charAt(j));
              }
          }
          // 4. 분리한 " "을 다시 넣어주며 반복한다.
          if (i != div.length-1)
              answer += " ";
      }
      return answer;
  }
}