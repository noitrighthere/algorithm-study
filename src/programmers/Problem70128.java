package programmers;

/**
 * 프로그래머스 내적
 * 유형: 수학
 * 난이도: LV1
 */

public class Problem70128 {
    public static void main(String[] args) {
        Solution70128 solution70128 = new Solution70128();
        solution70128.solution(new int[]{1, 2, 3, 4}, new int[]{-3, -1, 0, 2});
    }
}

class Solution70128 {
    public int solution(int[] a, int[] b) {
        int answer = 0;

        for (int i = 0; i < a.length; i++) {
            answer += a[i] * b[i];
        }

        return answer;
    }
}
