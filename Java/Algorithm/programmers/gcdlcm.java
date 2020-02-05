// [gcdlcm.java]
// 최대공약수와 최소공배수

class Solution {
  public int[] solution(int n, int m) {
      int[] answer = new int[2];
      // 최대공약수
      for (int i=Math.min(n,m); i>0; i--){
          if (n%i==0 && m%i==0) {
              answer[0]= i;
              break;
          }
      }
      // 최소공배수
      for (int i=Math.max(n,m); i<=n*m;i++){
          if (i%n==0 && i%m==0){
              answer[1]= i;
              break;
          }
      }
      return answer;
  }
}