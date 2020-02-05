// [collatz.java]
// 콜라츠 추측

class Solution {
  public int solution(int num) {
      int count = 0;
      long n = num;
      while (n != 1 && count < 500){
          count++;
          if (n % 2 == 0)
              n = n/2;
          else
              n = (n*3) + 1;
      }
      if (n==1)
          return count;
      else
          return -1;
  }
}