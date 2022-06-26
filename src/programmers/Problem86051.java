package programmers;

import java.util.ArrayList;
import java.util.List;

/**
 * 프로그래머스 없는 숫자 더하기
 * 월간 코드 챌린지 시즌3
 * 난이도: LV1
 */

public class Problem86051 {
    public static void main(String[] args) {
        Solution86051 solution86051 = new Solution86051();
        solution86051.solution(new int[]{1, 2, 3, 4, 6, 7, 8, 0});
    }
}

class Solution86051 {
    public int solution(int[] numbers) {
        int answer = 0;

        List<Integer> arr = new ArrayList<>();

        for (int number : numbers) {
            arr.add(number);
        }

        for (int i = 0; i <= 9; i++) {
            if (!arr.contains(i)) {
                answer += i;
            }
        }

        return answer;
    }
}