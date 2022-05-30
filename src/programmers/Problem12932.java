package programmers;

/**
 * 프로그래머스 자연수 뒤집어 배열로 만들기
 * 유형: 배열
 * 난이도: LV1
 */

public class Problem12932 {

    public static void main(String[] args) {
        Solution12932 solution12932 = new Solution12932();
        solution12932.solution(12345);
    }
}

class Solution12932 {
    public int[] solution(long n) {

        String str = String.valueOf(n);

        StringBuilder sb = new StringBuilder(str);
        String[] reverse = sb.reverse().toString().split("");

        int[] answer = new int[reverse.length];

        for (int i = 0; i < reverse.length; i++) {
            answer[i] = Integer.parseInt(reverse[i]);
        }

        return answer;
    }
}