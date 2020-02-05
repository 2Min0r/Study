// [peClass.java]
// 체육복

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int[] have = new int[n];
        for (int i=0; i<lost.length; i++)
            have[lost[i]-1]--;
        for (int i=0; i<reserve.length; i++)
            have[reserve[i]-1]++;
        
        for (int i=0; i<have.length; i++){
            if (have[i]==-1){
                if (i-1>=0 && have[i-1]==1){
                    have[i-1]--;
                }else if (i+1<have.length && have[i+1]==1){
                    have[i+1]--;
                }else{
                    answer--;
                }
            }
        }
        return answer;
    }
}