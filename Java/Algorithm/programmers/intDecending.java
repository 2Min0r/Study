// [int_decending.java]
// 정수 내림차순으로 배치하기

import java.util.*;
class Solution {
  public long solution(long n) {
      String s = Long.toString(n);
      int[] temp = new int[s.length()];
      // 1. 숫자를 문자로 변환 후 배열에 넣기
      for (int i=0; i<s.length(); i++) {
          temp[i] = Integer.parseInt(s.charAt(i)+"");
      }
      // 2. 오름차순 정렬
      Arrays.sort(temp);
      s = "";
      // 3. 내림차순 정렬
      for (int i=temp.length-1; i>=0; i--){
          s += temp[i];
      }
      // 4. return type으로 변환 후 반환
      long answer = Long.parseLong(s);
      return answer;
  }
}