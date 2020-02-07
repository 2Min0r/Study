// [evenOrOdd.java]
// 짝수와 홀수

class Solution {
  public String solution(int num) {
    // 1. 2로 나눠서 0이면 짝수
      if (num % 2 == 0)
          return "Even";
    // 2. 아니면 홀수
      else
          return "Odd";
  }
}