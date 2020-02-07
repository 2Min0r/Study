// [no_continuous.java]
// 같은 숫자는 싫어

import java.util.*;

public class Solution {
	public int[] solution(int []arr) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(arr[0]);
        
        // 1. 리스트의 맨 뒤 숫자를 확인하며 같지 않다면 리스트에 추가
        for (int i=0; i<arr.length; i++) {
            if (list.get(list.size()-1) != arr[i])
                list.add(arr[i]);
        }

        // 2. return type으로 변경 후 반환
        int[] answer = new int[list.size()];
        for (int i=0; i<list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
	}
}