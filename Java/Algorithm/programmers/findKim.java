// [findKim.java]
// 서울에서 김서방 찾기

class Solution {
  public String solution(String[] seoul) {
      String answer = "";

      // 1. 전체에서 Kim을 찾으면 종료
      for (int i=0; i<seoul.length; i++) {
          if (seoul[i].equals("Kim")) {
              answer = "김서방은 "+ i + "에 있다";
              break;
          }
      }
      // 2. Kim의 위치 출력
      return answer;
  }
}