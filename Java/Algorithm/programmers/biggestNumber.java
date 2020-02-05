// [biggestNumber.java]
// 가장 큰 수

import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        Integer[] array = new Integer[numbers.length];
        for (int i=0; i<numbers.length; i++) 
            array[i] = numbers[i];

        Arrays.sort(array, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                String tmp1 = o1.toString();
                String tmp2 = o2.toString();
                return (tmp2+tmp1).compareTo(tmp1+tmp2);
            }
        });

        String answer = "";
        for(int i=0; i<array.length; i++){
            answer += String.valueOf(array[i]); 
        }

        if("0".equals(answer.substring(0, 1)))
            return "0";

        return answer;
    }
}