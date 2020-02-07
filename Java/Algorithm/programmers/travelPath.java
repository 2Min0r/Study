// [travelPath.java]
// 여행경로

import java.util.*;
class Solution {
    public String[] solution(String[][] tickets) {
        String[] answer = new String[tickets.length*2-(tickets.length-1)];
        LinkedList<String> queue = new LinkedList<>();
        boolean[] chk = new boolean[tickets.length];
        int cnt = 0;
        // 1. ICN부터 시작하므로 ICN을 queue에 넣는다.
        queue.add("ICN");
        answer[cnt++] = "ICN";
        while(!queue.isEmpty()){
            String info = queue.poll();
            for(int i=0; i<tickets.length; i++){
                // 2. queue에서 꺼낸 값이 티켓의 출발지와 같고, 아직 경로에 넣지 않았다면, 추가한다.
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