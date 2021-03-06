// [bullsAndCows.java]
// 숫자 야구

import java.util.*;
class Solution {
    public int solution(int[][] baseball) {
        // 모든 경우의 수를 queue에 추가
        // queue에서 하나씩 빼가면서 해당하면 ok queue에 추가
        LinkedList<String> queue = new LinkedList<>();
        LinkedList<String> ok = new LinkedList<>();
        
        // 1. 모든 경우의 수를 queue에 추가
        for(int i=1; i<10; i++){
            for(int j=1; j<10; j++){
                for(int k=1; k<10; k++){
                    if(i != j && i != k && j!= k){
                        queue.add(String.valueOf(i*100+j*10+k));
                    }
                }
            }
        }
        
        while(!queue.isEmpty()){
            String info = queue.poll();
            boolean pass = true;

            // 2. queue에서 뺀 값의 스트라이크와 볼과 제시된 스트라이크와 볼 비교
            for(int i=0; i<baseball.length; i++){
                int s=0;
                int b=0;
                for(int j=0; j<info.length(); j++){
                    String temp = info.substring(j,j+1);
                    String target = String.valueOf(baseball[i][0]);
                    if (temp.equals(target.substring(j,j+1))) s++;
                    else if (target.contains(temp)) b++;
                }
                if (s != baseball[i][1] || b != baseball[i][2]){
                    pass=false;
                    break;
                }
            }
            // 3. 일치한다면, ok queue에 추가
            if (pass==true) ok.add(info);
            
        }
        // 4. 가능한 조합의 개수 출력
        int answer = ok.size();
        return answer;
    }
}