// [adder.java]
// 두 정수 사이의 합

class Solution {
  public long solution(int a, int b) {
      long answer = 0;
      // 1. 작은수부터 큰수까지의 범위를 더한다.
      for (int i = Math.min(a,b); i <= Math.max(a,b); i++){
          answer += i;
      }
      return answer;
          
  }
}