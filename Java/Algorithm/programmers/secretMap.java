// [secretMap.java]
// [1차]비밀지도

class Solution {
  public String[] solution(int n, int[] arr1, int[] arr2) {
      String[] answer = new String[n];
      // 1. 두 숫자를 이진수로 변환하여 합친다.
      for (int i=0; i<n; i++){
          String tmp = Integer.toBinaryString(arr1[i]|arr2[i]);
          answer[i] = tmp;
      }
      // 2. 빈 자릿수를 공백으로 채운 후, 0은 공백으로, 1은 #으로 변환한다.
      for (int i=0; i<n; i++){
          answer[i] = String.format("%"+n+"s",answer[i]);
          answer[i] = answer[i].replaceAll("0"," ");
          answer[i] = answer[i].replaceAll("1","#");
      }
      return answer;
  }
}