// [clearDivision.java]
// 나누어 떨어지는 숫자 배열

import java.util.*;

class Solution {
  public int[] solution(int[] arr, int divisor) {
      ArrayList<Integer> list = new ArrayList<>();

      // 1. 나누어 떨어지는 값 list에 추가
      for (int i=0; i < arr.length; i++) {
          if (arr[i] % divisor == 0) 
              list.add(arr[i]);
      }
      
      // 2. 없을 경우 -1 추가
      if (list.size() == 0)
          list.add(-1);
      
      // 3. list를 return type으로 변환
      int[] answer = new int[list.size()];
      for (int i = 0; i < list.size(); i++){
          answer[i] = list.get(i);
      }
      
      // 4. 오름차순 정렬
      Arrays.sort(answer);
      return answer;
  }
}