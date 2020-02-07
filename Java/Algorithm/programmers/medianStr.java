// [medianStr.java]
// 가운데 글자 가져오기

class Solution {
  public String solution(String s) {
    // 1. 짝수일 경우 두글자 가져오기
    if (s.length() % 2 == 0)
      return s.substring(s.length()/2-1, s.length()/2+1);
      // 2. 홀수일 경우 한글자 가져오기
    else
      return s.substring(s.length()/2, s.length()/2+1);
  }
}

