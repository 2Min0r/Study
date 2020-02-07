// [noCompletion.java]
// 완주하지 못한 선수

import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        // 1. 두 배열의 차이가 1개이기 때문에 다른 부분을 찾기 위해 정렬
        Arrays.sort(participant);
        Arrays.sort(completion);

        // 2. 참여선수와 완주선수 이름이 다르다면, 참여선수가 완주하지 못한 것
        for (int i=0; i < completion.length; i++) {
            if (participant[i].equals(completion[i])){
                continue;
            } else {
                return participant[i];
            }
        }
        // 3. 마지막 참여선수가 완주하지 못한 경우
        return participant[participant.length-1];
    }
}