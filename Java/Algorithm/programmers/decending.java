// [decending.java]
// 문자열 내림차순으로 배치하기

import java.util.Arrays;

class Solution {
  public String solution(String s) {
      String answer = "";
      // 1. 문자열 배열에 저장
      char[] sorted = s.toCharArray();
      // 2. 오름차순 정렬
      Arrays.sort(sorted);
      // 3. 거꾸로 문자열에 저장
      for (int i = sorted.length-1; i >= 0; i--){
          answer += sorted[i];
      }
      return answer;
  }
}