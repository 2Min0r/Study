// [average.java]
// 평균 구하기

class Solution {
  public double solution(int[] arr) {
      double answer = 0;
      int sum = 0;
      // 1. 전체 array의 합 구하기
      for (int i=0; i < arr.length; i++){
          sum += arr[i];
      }
      // 2. 합을 개수로 나누기 - 소수자리 표시해야 하므로 double
      answer = sum / (double)arr.length;
      return answer;
  }
}