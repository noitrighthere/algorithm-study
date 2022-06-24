package programmers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 프로그래머스 두 개 뽑아서 더하기
 * 월간 코드 챌린지 시즌1
 * 난이도: LV1
 */

public class Problem68644 {
    public static void main(String[] args) {
        Solution68644 solution68644 = new Solution68644();
        solution68644.solution(new int[]{2, 1, 3, 4, 1});
    }
}

class Solution68644 {
    public int[] solution(int[] numbers) {

        int temp = 0;
        List<Integer> arr = new ArrayList<>();

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                temp = numbers[i] + numbers[j];
                if (!arr.contains(temp)) {
                    arr.add(temp);
                }
            }
        }

        Collections.sort(arr);
        int[] answer = new int[arr.size()];

        for (int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i);
        }

        return answer;
    }
}
