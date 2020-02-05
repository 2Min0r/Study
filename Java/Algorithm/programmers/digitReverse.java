// [digitReverse.java]
// 자연수 뒤집어 배열로 만들기

import java.util.*;
class Solution {
  public int[] solution(long n) {
      String s = Long.toString(n);
      int[] answer = new int[s.length()];
      int i = 0;
      while (n > 0){
          answer[i]= (int)(n%10);
          n = n/10;
          i++;
      }
      return answer;
  }
}

import java.util.*;
class Solution {
  public int[] solution(long n) {
      ArrayList<Long> list = new ArrayList<>();
      while (n >= 10) {
          list.add(n % 10);
          n = n / 10;
      }
      list.add(n % 10);

      int[] answer = new int[list.size()];
      for (int j=0; j < list.size(); j++)
          answer[j] = Math.toIntExact(list.get(j));

      return answer;
  }
}