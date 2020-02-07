// [hideNumbers.java]
// 핸드폰 번호 가리기

class Solution {
  public String solution(String phone_number) {
      String answer = "";
      // 1. 뒷자리 4개만큼 * 만들기
      for (int i=0; i<phone_number.length()-4; i++){
          answer += "*";
      }
      // 2. 앞자리 + 뒷자리 4개 * 연결하기
      answer += phone_number.substring(phone_number.length()-4, phone_number.length());
      return answer;
  }
}