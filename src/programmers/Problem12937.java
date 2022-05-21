package programmers;

/**
 * 프로그래머스 짝수와 홀수
 * 유형: 수학
 * 난이도: LV1
 */

public class Problem12937 {

    public static void main(String[] args) {
        Solution12937 solution12937 = new Solution12937();
        System.out.println("solution12937 = " + solution12937.solution(3));
    }
}

class Solution12937 {
    public String solution(int num) {
        String answer = "";

        if (num % 2 == 0) {
            answer = "Even";
        } else {
            answer = "Odd";
        }
        return answer;
    }
}