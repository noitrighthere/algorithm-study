package programmers;

import java.util.*;

/**
 * 프로그래머스 나머지가 1이 되는 수 찾기
 * 월간 코드 챌린지 시즌3
 * 난이도: LV1
 */

public class Problem87389 {
    public static void main(String[] args) {
        Solution87389 solution87389 = new Solution87389();
        solution87389.solution(12);
    }
}

class Solution87389 {
    public int solution(int n) {
        int answer = 0;
        List<Integer> arr = new ArrayList<>();

        for (int i = 1; i < n; i++) {
            if (n % i == 1) {
                arr.add(i);
            }
        }

        answer = Collections.min(arr);

        return answer;
    }
}