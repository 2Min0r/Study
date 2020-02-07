// [functionDev.java]
// 기능 개발

import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        LinkedList<Integer> queue = new LinkedList<>();
        LinkedList<Integer> temp = new LinkedList<>();
        //1. queue에 전체 작업을 넣는다.
        for (int i=0; i<progresses.length; i++){
            queue.add(i);
        }
        int time = 0, cur=0, complete=0;
        while(!queue.isEmpty()){
            Integer info = queue.peek();
            //2. 작업이 완료되었다면, 다음 queue가 배포가능한지 확인한다.
            if(progresses[info]+(time*speeds[info])>=100){
                queue.poll();
                complete++;
                while(!queue.isEmpty() && progresses[queue.peek()]+(time*speeds[queue.peek()])>=100){
                    queue.poll();
                    complete++;
                }
                //3. 배포가능한 작업 수만큼 추가하고, complete를 초기화한다.
                temp.add(complete);
                complete=0;
            }
            time++;
        }
        //4. 모든 작업이 완료되었다면, 하루 배포개수를 int[]에 넣고 반환한다.
        int[] answer = new int[temp.size()];
        for(int i=0; i<temp.size(); i++){
            answer[i]=temp.get(i);
        }
        return answer;
    }
}