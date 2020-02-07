// [top.java]
// 탑

import java.util.*;
class Solution {
    public int[] solution(int[] heights) {
        // 스택으로 구현
        // 전체 heights를 넣고
        // 마지막 원소를 pop하고, 그 전까지의 원소 살펴서 크면 바로 break후 배열에 넣기
        int[] answer = new int[heights.length];
        Stack<top> stack = new Stack<>();
        int cnt = heights.length-1;
        // 1. 스택으로 전체 heights 넣기
        for(int i=0; i<heights.length; i++){
            stack.push(new top(i, heights[i]));
        }
        // 2. 하나씩 빼서 뒤에서 앞으로 가면서 타워가 높다면 break
        while(!stack.empty()){
            top info = stack.pop();
            for (int i=cnt; i>-1; i--){
                if(info.height<heights[i]){
                    answer[info.idx]=i+1;
                    break;
                }
            }
            cnt--;
        }
        return answer;
    }
}
class top {
    int idx;
    int height;
    top(int idx, int height){
        this.idx = idx;
        this.height = height;
    }
}