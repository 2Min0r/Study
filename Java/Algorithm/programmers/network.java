// [network.java]
// 네트워크

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        // 1. 확인한 컴퓨터인지 체크할 배열 생성
        boolean[] chk = new boolean[n];
        // 2. 확인하지 않은 컴퓨터 차례로 확인
        for (int i=0; i<n; i++){
            if(!chk[i]){
                // 3. 연결된 컴퓨터들 확인하며 network 개수세기
                dfs(computers, chk, i);
                answer++;
            }
        }
        return answer;
    }
    public void dfs(int[][] computers, boolean[] chk, int start){
        chk[start] = true;
        for(int i=0; i<computers.length; i++){
            if(computers[start][i]==1 && !chk[i]){
                dfs(computers, chk, i);
            }
        }
    }
}