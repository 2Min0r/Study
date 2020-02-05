// [failureRate.java]
// 실패율

import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        HashMap<Integer, Double> failmap = new HashMap<>();
        int[] fail = new int[N+1];

        for (int i=0; i<stages.length; i++){
            for (int j=0; j<stages[i]; j++){
                fail[j]++;
            }
        }
        for (int i=0; i<answer.length; i++){
            failmap.put((fail[i]-fail[i+1])/ Double.valueOf(fail[i]), i);
        }

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