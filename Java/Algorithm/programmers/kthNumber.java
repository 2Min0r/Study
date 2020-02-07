// [kthNumber.java]
// K번째수
import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i=0; i<commands.length; i++) {
            // 1. 정렬해야하는 범위까지 자름
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            // 2. 오름차순 정렬
            Arrays.sort(temp);
            System.out.println(temp[0]);
            // 3. 정렬 후 k번째 수를 answer에 추가
            answer[i] = temp[commands[i][2]-1];
        }
        return answer;
    }
}