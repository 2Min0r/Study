// [secretMap.java]
// [1차]비밀지도

class Solution {
  public String[] solution(int n, int[] arr1, int[] arr2) {
      String[] answer = new String[n];
      for (int i=0; i<n; i++){
          String tmp = Integer.toBinaryString(arr1[i]|arr2[i]);
          answer[i] = tmp;
      }
      for (int i=0; i<n; i++){
          answer[i] = String.format("%"+n+"s",answer[i]);
          answer[i] = answer[i].replaceAll("0"," ");
          answer[i] = answer[i].replaceAll("1","#");
      }
      return answer;
  }
}