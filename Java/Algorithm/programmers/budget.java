// [budget.java]
// 예산

import java.util.*;
class Solution {
  public int solution(int[] d, int budget) {
      int answer = 0;

      // 1. 예산이 가장 작은 순서로 정렬
      Arrays.sort(d);

      // 2. 지원할 수 있는 부서 수 구하기
      for (int i=0; i<d.length; i++){
          if (budget-d[i]>=0){
              answer++;
              budget -= d[i];
          }
          if (budget < 0)
              break;
      }
      return answer;
  }
}