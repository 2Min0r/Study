// [sumDivisor.java]
// 약수의 합

class Solution {
  public int solution(int n) {
      int answer = 0;
      // 1. n/2까지만 값을 나눠주며 약수를 더한다.
      for (int i = 1; i <= n/2; i++){
          if (n % i == 0)
              answer += i;
      }
      // 2. 자신의 수를 더한후 반환한다.
      return answer+n;
  }
}