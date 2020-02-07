// [digitReverse.java]
// 자연수 뒤집어 배열로 만들기

import java.util.*;
class Solution {
  public int[] solution(long n) {
      // 1. 문자열 변환
      String s = Long.toString(n);
      int[] answer = new int[s.length()];
      // 2. 문자열은 뒤에서부터 잘라서 정수로 배열에 앞에서부터 넣는다.
      for (int i=s.length()-1, j=0; i>-1; i--, j++){
          answer[j]= Integer.valueOf(s.substring(i,i+1));
      }
      return answer;
  }
}

import java.util.*;
class Solution {
  public int[] solution(long n) {
      String s = Long.toString(n);
      int[] answer = new int[s.length()];
      int i = 0;
      // 2. 
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