package programmers;


import java.util.Arrays;

/**
 * 프로그래머스 제일 작은 수 제거하기
 * 유형: 배열
 * 난이도: LV1
 */

public class Problem12935 {

    public static void main(String[] args) {

        Solution12935 solution12935 = new Solution12935();

        int arr[] = {4, 3, 2, 1};
    }
}

class Solution12935 {
    public int[] solution(int[] arr) {

       if (arr.length == 1) {
           return new int[]{-1};
       }

       int minIdx = 0;

       for (int i = 0; i < arr.length; i++) {
           if (arr[minIdx] > arr[i]) {
               minIdx = i;
           }
       }

       int[] answer = new int[arr.length-1];
       int cnt = 0;

       for (int i = 0; i < arr.length; i++) {
           if (i == minIdx) {
               continue;
           }
           answer[cnt++] = arr[i];
       }

       return answer;
    }
}