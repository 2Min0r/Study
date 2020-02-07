// [strangeSort.java]
// 문자열 내 마음대로 정렬하기

import java.util.Arrays;
class Solution {
  public String[] solution(String[] strings, int n) {
      // 1. 정렬기준이 되는 문자를 맨 앞으로 가져온다.
      for (int i=0; i<strings.length; i++){
          strings[i] = strings[i].substring(n,n+1) + strings[i];
      }
      // 2. 정렬
      Arrays.sort(strings);
      // 3. 정렬기준으로 쓴 문자를 삭제한다.
      for (int i=0; i < strings.length; i++){
          strings[i] = strings[i].substring(1,strings[i].length());
      }
      return strings;
  }
}