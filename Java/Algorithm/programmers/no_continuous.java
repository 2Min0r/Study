// [no_continuous.java]
// 같은 숫자는 싫어

import java.util.*;

public class Solution {
	public int[] solution(int []arr) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(arr[0]);
        
        for (int i=0; i<arr.length; i++) {
            if (list.get(list.size()-1) != arr[i])
                list.add(arr[i]);
        }

        int[] answer = new int[list.size()];
        
        for (int i=0; i<list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
	}
}