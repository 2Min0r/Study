// [sumDigit.java]
// 자릿수 더하기

public class Solution {
    public int solution(int n) {
        if (n < 10)
            return n % 10;
        return n % 10 + solution(n/10);
    }
}