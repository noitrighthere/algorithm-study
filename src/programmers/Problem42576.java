package programmers;

import java.util.Arrays;

/**
 * 프로그래머스 완주하지 못한 선수
 * 유형: 해시
 * 난이도: LV1
 */

public class Problem42576 {
    public static void main(String[] args) {
        Solution42576 solution42576 = new Solution42576();
        solution42576.solution(new String[]{"leo", "kiki", "eden"}, new String[]{"eden", "kiki"});
    }
}

class Solution42576 {
    public String solution(String[] participant, String[] completion) {

        String answer = "";

        Arrays.sort(participant);
        Arrays.sort(completion);

        for (int i = 0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                answer += participant[i];
                return answer;
            }
        }

        answer += participant[participant.length - 1];
        return answer;
    }
}