// [discController.java]
// 디스크 컨트롤러

import java.util.*;
public class Job implements Comparable<Job> {
    int start;
    int workTime;
    Job(int start, int time){
        this.start = start;
        this.time = time;
    }
    @Override
    public int compareTo(Job o) {
        if (this.workTime < o.workTime) return -1;
        else if (this.workTime == o.workTime ) {
            if (this.start < o.start) return -1;
            else return 1;
        }
        else return 1;
    }
}

class Solution {
    public int solution(int[][] jobs){
        PriorityQueue<Job> pq = new PriorityQueue<>();
        List<Job> list = new LinkedList<>();

        for (int i=0; i<jobs.length; i++){
            pd.add(new Job(jobs[i][0], jobs[i][1]));
        }

        for (int i=0; i< jobs.length; i++){
            list.add(pq.poll());
        }

        int time = 0;
        int sum = 0;
        while (list.size()>0){
            for (int i=0; i<list.size(); i++){
                if (time>=list.get(i).start){
                    time+= list.get(i).workTime;
                    sum+= time-list.get(i).start;
                    list.remove(i);
                    break;
                }
                if (i==list.size()-1) time++;
            }
        }
        int answer = (sum/jobs.length);
        return answer;
    }
}