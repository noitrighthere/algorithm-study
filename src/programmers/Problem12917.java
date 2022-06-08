package programmers;

import java.util.Arrays;

/**
 * 프로그래머스 문자열 내림차순으로 배치하기
 * 유형: 문자열
 * 난이도: LV1
 */

public class Problem12917 {
    public static void main(String[] args) {
        Solution12917 solution12917 = new Solution12917();
        solution12917.solution("Zbcdefg");
    }
}

class Solution12917 {
    public String solution(String s) {
        String answer = "";

        char[] arr = s.toCharArray();   // String s를 char[]로 만듦
        Arrays.sort(arr);               // 오름차순으로 정렬

        StringBuilder sb = new StringBuilder(new String(arr));
        answer = sb.reverse().toString();   // 오름차순을 반대로 해서 내림차순으로 정렬

        return answer;
    }
}