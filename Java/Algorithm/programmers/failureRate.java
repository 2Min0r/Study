// [failureRate.java]
// 실패율

import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        HashMap<Integer, Double> failmap = new HashMap<>();
        int[] fail = new int[N+1];

        // 1. 각 페이지에 도달한 플레이어수 구함
        for (int i=0; i<stages.length; i++){
            for (int j=0; j<stages[i]; j++){
                fail[j]++;
            }
        }

        // 2. 각 스테이지별 실패율을 hashmap에 저장
        for (int i=0; i<answer.length; i++){
            failmap.put(i+1, (fail[i]-fail[i+1])/ Double.valueOf(fail[i]));
        }
        
        // 3. 실패율을 기준으로 내림차순으로 스테이지 정렬
        for (int i=0; i<N; i++){
            double max = -1;
            int maxkey = 0;
            for (Integer key : failmap.keySet()){
                if(max < failmap.get(key)){
                    max = failmap.get(key);
                    maxkey = key;
                }
            }
            answer[i] = maxkey;
            failmap.remove(maxkey);
        }
        return answer;
    }
}