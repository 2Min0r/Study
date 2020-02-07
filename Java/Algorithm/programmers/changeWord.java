// [chagneWord.java]
// 단어 변환
import java.util.*;
class Solution{
    public int solution(String begin, String target, String[] words){
        // 1. 단어와 단어의 변화 횟수를 셀 class 생성
        LinkedList<wordTimes> queue = new LinkedList<>();
        boolean[] chk = new boolean[words.length];

        // 2. 시작을 기준으로 queue에서 하나씩 바뀐 단어 반복
        queue.add(new wordTimes(begin, 0));
        while(!queue.isEmpty()){
            wordTimes info = queue.poll();
            // 3. 단어가 target이랑 같을 경우 종료
            if(info.word.equals(target)) return info.times;
            for(int i=0; i<words.length; i++){
                // 2-1. 추가된 적이 없고, 하나만 바뀐 단어일 경우 queue에 삽입
                if(!chk[i] && checkword(info.word, words[i])){
                    chk[i] = true;
                    queue.add(new wordTimes(words[i], info.times+1));
                }
            }
        }
        // 3. 바꿀 수 없을 경우 0 출력
        return 0;
    }
    public boolean checkword(String begin, String word){
        int cnt=0;
        // 1. 한단어씩 비교해서 다를 경우 카운트 증가
        for(int i=0; i<begin.length(); i++){
            String a = begin.substring(i,i+1);
            String b = word.substring(i,i+1);
            if(!a.equals(b)) cnt++;
        }
        // 2. 카운트가 1일 경우 == 한단어만 바뀌었을 경우 true
        if (cnt==1) return true;
        else return false;
    }
}
class wordTimes {
    String word;
    int times;
    wordTimes(String word, int times){
        this.word = word;
        this.times = times;
    }
}