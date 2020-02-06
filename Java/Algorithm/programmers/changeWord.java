// [chagneWord.java]
// 단어 변환
import java.util.*;
class Solution{
    public int solution(String begin, String target, String[] words){
        LinkedList<wordTimes> queue = new LinkedList<>();
        boolean[] chk = new boolean[words.length];
        queue.add(new wordTimes(begin, 0));
        while(!queue.isEmpty()){
            wordTimes info = queue.poll();
            if(info.word.equals(target)) return info.times;
            for(int i=0; i<words.length; i++){
                if(!chk[i] && checkword(info.word, words[i])){
                    chk[i] = true;
                    queue.add(new wordTimes(words[i], info.times+1));
                }
            }
        }
        return 0;
    }
    public boolean checkword(String begin, String word){
        int cnt=0;
        for(int i=0; i<begin.length(); i++){
            String a = begin.substring(i,i+1);
            String b = word.substring(i,i+1);
            if(!a.equals(b)) cnt++;
        }
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