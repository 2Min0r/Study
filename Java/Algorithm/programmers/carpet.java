// [carpet.java]
// 카펫 

class Solution {
    public int[] solution(int brown, int red) {
        int width = 0;
        int height = 0;
        for(int i=1; i<=red/2+1; i++) {
            width = i;            
            height = (red%i==0) ? red/i:red/i+1;
            if(2*width + 2*height + 4 == brown) break;
        }
        int[] answer = {Math.max(width, height)+2, Math.min(width, height)+2};
        return answer;
    }
}