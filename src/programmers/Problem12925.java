package programmers;

/**
 * 프로그래머스 문자열을 정수로 바꾸기
 * 유형: 문자열
 * 난이도: LV1
 */

public class Problem12925 {

    public static void main(String[] args) {
        Solution12925 solution12925 = new Solution12925();
        solution12925.solution("1234");
    }
}

class Solution12925 {
    public int solution(String s) {
        int answer = 0;
        answer = Integer.parseInt(s);
        return answer;
    }
}