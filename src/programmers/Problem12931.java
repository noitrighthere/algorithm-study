package programmers;

import java.util.*;

/**
 * 프로그래머스 자릿수 더하기
 * 유형: 수학
 * 난이도: LV1
 */

public class Problem12931 {
    public static void main(String[] args) {
        Solution12931 solution12931 = new Solution12931();
        solution12931.solution(987);
    }
}

class Solution12931 {
    public int solution(int n) {
        int answer = 0;

        while (n > 0) {
            answer += n % 10;
            n /= 10;
        }

        return answer;
    }
}