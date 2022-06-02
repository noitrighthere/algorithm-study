package programmers;

import java.util.Comparator;

/**
 * 프로그래머스 정수 내림차순으로 배치하기
 * 유형: 배열
 * 난이도: LV1
 */

public class Problem12933 {
    public static void main(String[] args) {

        Solution12933 solution12933 = new Solution12933();
        System.out.println(solution12933.solution(118372));
    }
}

class Solution12933 {
    public long solution(long n) {
        StringBuilder stringBuilder = new StringBuilder();
        String.valueOf(n).chars().mapToObj(ch -> (char)ch).sorted(Comparator.reverseOrder()).forEach(ch -> stringBuilder.append(ch));

        return Long.parseLong(stringBuilder.toString());
    }
}