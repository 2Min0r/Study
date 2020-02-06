// [travelPath.java]
// 여행경로

import java.util.*;
class Solution {
    public String[] solution(String[][] tickets) {
        // dfs를 사용한다.
        // dfs는 큐? 
        String[] answer = new String[tickets.length*2-(tickets.length-1)];
        LinkedList<String> queue = new LinkedList<>();
        boolean[] chk = new boolean[tickets.length];
        int cnt = 0;
        
        
        queue.add("ICN");
        answer[cnt++] = "ICN";
        while(!queue.isEmpty()){
            String info = queue.poll();
            for(int i=0; i<tickets.length; i++){
                if(tickets[i][0].equals(info) && !chk[i]){
                    System.out.println(cnt);
                    chk[i]= true;
                    answer[cnt++] = tickets[i][1];
                    queue.add(tickets[i][1]);
                }
            }
        }
        return answer;
    }

}