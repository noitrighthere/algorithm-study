package programmers;

/**
 * 프로그래머스 수박수박수박수박수박?
 * 유형: 문자열
 * 난이도: LV1
 */

public class Problem12922 {
    public static void main(String[] args) {
        Solution12922 solution12922 = new Solution12922();
        solution12922.solution(3);
    }
}

class Solution12922 {
    public String solution(int n) {
        String answer = "";

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
               answer += "수";
            } else {
                answer += "박";
            }
        }

        return answer;
    }
}
