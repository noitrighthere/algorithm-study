package programmers;

/**
 * 프로그래머스 문자열 다루기 기본
 * 유형: 문자열
 * 난이도: LV1
 */

public class Problem12918 {
    public static void main(String[] args) {
        Solution12918 solution12918 = new Solution12918();
        solution12918.solution("122342");
    }
}

class Solution12918 {
    public boolean solution(String s) {
        boolean answer = true;
        String str = s;
        char temp;

        // 문자열 s의 길이가 4 또는 6이 아닌 경우 answer = false
        if (!(s.length() == 4 || s.length() == 6)) {
            answer = false;
        }

        for (int i = 0; i < s.length(); i++) {

             temp = str.charAt(i);
            // temp가 0 ~ 9 사이의 숫자가 아닌 경우 answer = false
            if (!('0' <= temp && temp <= '9')) {
                answer = false;
            }
        }

        System.out.println(answer);

        return answer;
    }
}