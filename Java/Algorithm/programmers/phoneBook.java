// [phoneBook.java]
// 전화번호 목록

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        // 1. 각 전화번호를 순회한다.
        for(int i=0; i<phone_book.length-1; i++){
            String info = phone_book[i];
            // 2. 순회중인 전화번호 외의 전화번호를 순회한다.
            for(int j=0; j<phone_book.length; j++){
                String temp = phone_book[j];
                if(info.equals(temp)) continue;
                // 3. 전화번호가 더 긴 것을 바탕으로 잘라서 접두어인지 비교한다.
                if(info.length()<=temp.length()){
                    if(temp.substring(0,info.length()).equals(info)){
                        answer = false;
                        break;
                    }
                }else{
                    if(info.substring(0,temp.length()).equals(temp)){
                        answer = false;
                        break;
                    }
                }
            }
        }
        return answer;
    }
}