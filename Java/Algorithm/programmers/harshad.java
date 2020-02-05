// [harshad.java]
// 하샤드 수

class Solution {
    public int digitSum(int n) {
        if (n < 10)
            return n % 10;
        return n % 10 + digitSum(n/10);
    }
    
    public boolean solution(int x) {
      int sum = digitSum(x);
      if (x % sum == 0)
          return true;
      else
          return false;
    }
}