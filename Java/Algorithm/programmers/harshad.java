// [harshad.java]
// 하샤드 수

class Solution {
    // 1. 각 자릿수의 합 구하기
    public int digitSum(int n) {
        if (n < 10)
            return n % 10;
        return n % 10 + digitSum(n/10);
    }
    
    public boolean solution(int x) {
      int sum = digitSum(x);
      // 2. x가 자릿수의 합으로 나누어떨어지면 하샤드수
      if (x % sum == 0)
          return true;
      else
          return false;
    }
}