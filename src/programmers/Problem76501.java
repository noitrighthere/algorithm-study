package programmers;

/**
 * 프로그래머스 음양 더하기
 * 월간 코드 챌린지 시즌2
 * 난이도: LV1
 */

public class Problem76501 {

    public static void main(String[] args) {
        Solution76501 solution76501 = new Solution76501();
        int[] ints = {4, 7, 12};
        boolean[] signs = {true, false, true};
        solution76501.solution(ints, signs);

    }
}

class Solution76501 {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;

        for (int i = 0; i < absolutes.length; i++) {
            if (signs[i]) {
                answer += absolutes[i];
            } else {
                answer -= absolutes[i];
            }
        }
        System.out.println(answer);

        return answer;
    }
}
