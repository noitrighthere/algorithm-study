package programmers;

/**
 * 프로그래머스 행렬의 덧셈
 * 유형: 배열
 * 난이도: LV1
 */

public class Problem12950 {

    public static void main(String[] args) {

        int arr1[][] = {{1, 2}, {2, 3}};
        int arr2[][] = {{3, 4}, {5, 6}};

        Solution12950 solution12950 = new Solution12950();
        solution12950.solution(arr1, arr2);
    }
}

class Solution12950 {
    public int[][] solution(int[][] arr1, int[][] arr2) {

        int[][] answer = new int[arr1.length][arr1[0].length];

        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr1[0].length; j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }

        return answer;
    }
}