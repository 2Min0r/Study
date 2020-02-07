// [targetNumber.java]
// 타겟 넘버

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = dfs(numbers, 0, 0, target);
        return answer;
    }

    public int dfs(int[] numbers, int node, int sum, int target) {
        // sum과 node를 통해 다음값을 더하기 빼기를 하며 타겟넘버를 찾는다.
        // node가 전체 배열을 살폈을 때, sum이 target과 같다면 1, 아니라면 0을 해준다.
        // 총 가능한 경우의 수의 개수를 알 수 있다.
        if(node == numbers.length) {
            if (sum==target) return 1;
            else return 0;
        }
        return dfs(numbers, node + 1, sum + numbers[node], target) +
            dfs(numbers, node + 1, sum - numbers[node], target);
    }
}