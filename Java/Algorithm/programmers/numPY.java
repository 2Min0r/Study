// [numPY.java]
// 문자열 내 p와 y의 개수

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i)=='p' || s.charAt(i)=='P'){
                p++;
            }else if (s.charAt(i)=='y' || s.charAt(i)=='Y'){
                y++;
            }
        }
        return p==y;
    }
}