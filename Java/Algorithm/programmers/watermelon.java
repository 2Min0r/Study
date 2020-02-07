// [watermelon.java]
// 수박수박수박수박수박수?

class Solution {
  public String solution(int n) {
    // 수박이 두 글자이므로, n/2+1만큼 반복한 후, n의 길이만큼 잘라준다.
    String answer = "수박".repeat(n/2+1);
    return answer.substring(0,n);
  }
}