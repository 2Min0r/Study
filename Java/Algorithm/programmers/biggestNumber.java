// [biggestNumber.java]
// 가장 큰 수

import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // 1. sort를 위해 Integer[]로 변환
        Integer[] array = new Integer[numbers.length];
        for (int i=0; i<numbers.length; i++) 
            array[i] = numbers[i];

        // 2. 문자열 변환 후 문자열조합하여 정렬
        Arrays.sort(array, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                String tmp1 = o1.toString();
                String tmp2 = o2.toString();
                return (tmp2+tmp1).compareTo(tmp1+tmp2);
            }
        });

        // 3. 문자열로 변환
        String answer = "";
        for(int i=0; i<array.length; i++){
            answer += String.valueOf(array[i]); 
        }
        
        // 4. 문자열이 0000.. 일 경우 0으로 반환
        if("0".equals(answer.substring(0, 1)))
            return "0";

        return answer;
    }
}