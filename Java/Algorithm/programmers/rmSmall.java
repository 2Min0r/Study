// [rmSmall.java]
// 제일 작은 수 제거하기

import java.util.*;
class Solution {
  public int[] solution(int[] arr) {
      int min = arr[0];
      for (int i=1; i<arr.length; i++){
          if (arr[i] < min) {
              min = arr[i];
          }
      }
      if (arr.length-1 == 0) {
          int[] answer = {-1};
          return answer;
      }
      int[] answer = new int[arr.length-1];
      for(int i=0, j=0; i < arr.length; i++){
          if (arr[i]==min)
              continue;
          else{
              answer[j] = arr[i];
              j++;
              }
      }
      return answer;
  }
}