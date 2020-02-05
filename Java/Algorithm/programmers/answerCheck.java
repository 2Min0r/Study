// [answerCheck.java]
// 모의고사

import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] answer = new int[3], student1 = {1,2,3,4,5}, student2 = {2,1,2,3,2,4,2,5}, student3 = {3,3,1,1,2,2,4,4,5,5};
        int max = 0;
        for (int i=0; i<answers.length; i++) {
            if (answers[i] == student1[i%student1.length])
                answer[0]++;
            if (answers[i] == student2[i%student2.length])
                answer[1]++;
            if (answers[i] == student3[i%student3.length])
                answer[2]++;
        }
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=0; i<3; i++) {
            if (max == answer[i])
                list.add(i+1);
            else if (max < answer[i]) {
                list.clear();
                list.add(i+1);
                max = answer[i];
            }
        }
        int[] higher = new int[list.size()];
        for (int i=0; i<list.size();i++){
            higher[i]= list.get(i);
        }
        return higher;
    }
}