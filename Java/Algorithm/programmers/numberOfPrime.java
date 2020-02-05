// [numberOfPrime.java]
// 소수 찾기

import java.util.*;
class Solution {
  public int solution(int n) {
      int answer = 0;
      boolean[] prime = new boolean[n+1];
      Arrays.fill(prime, true);
      
      for (int i = 2; i<= n; i++){
          if (prime[i] == true){
              answer++;
              for (int j = i*2; j <= n; j+=i) {
                  prime[j] = false;
              }
          }
      }
      return answer;
  }
}