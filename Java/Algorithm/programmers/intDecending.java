// [int_decending.java]
// 정수 내림차순으로 배치하기

import java.util.*;
class Solution {
  public long solution(long n) {
      String s = Long.toString(n);
      int[] temp = new int[s.length()];
      for (int i=0; i<s.length(); i++) {
          temp[i] = Integer.parseInt(s.charAt(i)+"");
      }
      Arrays.sort(temp);
      s = "";
      for (int i=temp.length-1; i>=0; i--){
          s += temp[i];
      }
      long answer = Long.parseLong(s);
      return answer;
  }
}