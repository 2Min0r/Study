// [nextSquare.java]
// 정수 제곱근 판별

class Solution {
  public long solution(long n) {

      if (Math.sqrt(n) % 1 != 0) {
          return (long)-1;
      }
      else
          return (long)Math.pow(Math.sqrt(n)+1,2);

  }
}