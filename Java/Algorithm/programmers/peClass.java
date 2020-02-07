// [peClass.java]
// 체육복

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int[] have = new int[n];
        // 1. 체육복을 잃어버린 사람 개수 -1
        for (int i=0; i<lost.length; i++)
            have[lost[i]-1]--;
        // 2. 체육복을 하나 더 가지고 있는 사람 +1
        // 이를 통해 가지고 있는 사람이 잃어버린다면 0이 되므로 처리 가능
        for (int i=0; i<reserve.length; i++)
            have[reserve[i]-1]++;
        
        // 3. 양 옆을 확인하며 빌리지 못한다면 참여하지 못하므로 answer-1
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
        // 4. 체육시간 참여가능 학생 수 반환
        return answer;
    }
}