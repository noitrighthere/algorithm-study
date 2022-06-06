package programmers;

/**
 * 프로그래머스 약수의 합
 * 유형: 수학
 * 난이도: LV1
 */

public class Problem12928 {
    public static void main(String[] args) {
        Solution12928 solution12928 = new Solution12928();
        solution12928.solution(12);
    }
}

class Solution12928 {
    public int solution(int n) {
        int answer = 0;

        for (int i = 1; i <= n; i++) {

            if (n % i == 0) {
                answer += i;
            }
        }

        return answer;
    }
}
