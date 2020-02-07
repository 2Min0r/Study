// [collatz.java]
// 콜라츠 추측

class Solution {
  public int solution(int num) {
      int count = 0;
      // 값이 커지므로 long으로 변환
      long n = num;
      // 1. 1이 될때까지 반복하되, 500번 반복시 멈춤
      while (n != 1 && count < 500){
          count++;
          // 2. 짝수일 경우 2로 나누기
          if (n % 2 == 0)
              n = n/2;
          // 2. 홀수일 경우 3곱하고 1더하기
          else
              n = (n*3) + 1;
      }
      // 3. 1일 경우 반복횟수 return
      if (n==1)
          return count;
      else
          return -1;
  }
}