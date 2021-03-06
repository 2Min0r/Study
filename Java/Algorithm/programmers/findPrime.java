// [findPrime.java]
// 소수 찾기

import java.util.*;

class Solution {
    public int solution(String numbers){
        // 문자(숫자)를 키로, 그 갯수를 밸류로 한다.
        // 숫자 조합을 만들어서 큐에 넣는다.
        // 큐에서 꺼내면서 순열을 per queue에 push

        HashMap<String, Integer> hm = new HashMap<>();
        LinkedList<String> queue = new LinkedList<>();
        LinkedList<String> per = new LinkedList<>();
        
        // 1. 숫자를 한 글자씩 queue에 넣는다.
        for(int i=0; i<numbers.length(); i++){
            String temp = numbers.substring(i,i+1);
            queue.add(temp);
            hm.put(temp, hm.getOrDefault(temp, 0)+1);
        }

        // 2. 숫자의 조합을 만들어 중복되지 않으면 per queue에 넣는다.
        while(!queue.isEmpty()){
            String info = queue.poll();
            per.add(info);

            for(int i=0; i<numbers.length(); i++){
                String temp = numbers.substring(i,i+1);
                int a = 0;
                for(int j=0; j<info.length(); j++){
                    String f = info.substring(j,j+1);
                    if(f.equals(temp)) a++;
                }
                if (a < hm.get(temp)){
                    temp = info + temp;
                    queue.add(temp);
                }
            }
        }
        // 3. per queue의 조합이 소수라면 answer에 넣는다.
        LinkedList<Integer> answers = new LinkedList<>();
        for(String temp : per) {
            Integer what = Integer.parseInt(temp);
            if(what == 1 || what == 0) continue;
            if(answers.contains(what)) continue;
            boolean pass = true;
            for(int i=2; i<what; i++){
                if(what % i == 0){
                    pass = false;
                    break;
                }
            }
            if(pass == true){
                answers.add(what);
            }
        }

        // 4. 소수의 개수를 출력한다.
        int answer = answers.size();
        return answer;
    }
}
