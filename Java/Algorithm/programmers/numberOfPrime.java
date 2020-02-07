// [numberOfPrime.java]
// 소수 찾기

import java.util.*;
class Solution {
  public int solution(int n) {
      int answer = 0;
      boolean[] prime = new boolean[n+1];
      // 1. 전체 배열을 true로 채움
      Arrays.fill(prime, true);

      // 2. 소수일 경우 false로 변경
      for (int i = 2; i<= n; i++){
          if (prime[i] == true){
              answer++;
              // 2-1. 현재 값의 배수를 false로 변경
              for (int j = i*2; j <= n; j+=i) {
                  prime[j] = false;
              }
          }
      }
      return answer;
  }
}