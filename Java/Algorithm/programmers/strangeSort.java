// [strangeSort.java]
// 문자열 내 마음대로 정렬하기

import java.util.Arrays;
class Solution {
  public String[] solution(String[] strings, int n) {
      for (int i=0; i<strings.length; i++){
          strings[i] = strings[i].substring(n,n+1) + strings[i];
      }
      Arrays.sort(strings);
      for (int i=0; i < strings.length; i++){
          strings[i] = strings[i].substring(1,strings[i].length());
      }
      return strings;
  }
}