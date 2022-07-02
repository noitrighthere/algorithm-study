package programmers;

/**
 * 프로그래머스 최소직사각형
 * 위클리 챌린지
 * 난이도: LV1
 */
public class Problem86491 {
    public static void main(String[] args) {
        int[][] arr = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
        Solution86491 solution86491 = new Solution86491();
        solution86491.solution(arr);
    }
}

class Solution86491 {
    public int solution(int[][] sizes) {
        int answer = 0;
        int height = 0;
        int width = 0;

        for (int i = 0; i < sizes.length; i++) {
            int w = Math.max(sizes[i][0], sizes[i][1]);
            int h = Math.min(sizes[i][0], sizes[i][1]);
            width = Math.max(width, w);
            height = Math.max(height, h);
        }

        answer = height * width;

        return answer;
    }
}
