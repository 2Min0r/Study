// [nextSquare.java]
// 정수 제곱근 판별

class Solution {
  public long solution(long n) {
    // 1. 제곱근이 정수가 아니라면 -1 출력
    if (Math.sqrt(n) % 1 != 0) {
      return (long)-1;
    }
    // 2. 제곱근이 정수가 아니라면 제곱근+1을 제곱하여 출력
    else
      return (long)Math.pow(Math.sqrt(n)+1,2);

  }
}