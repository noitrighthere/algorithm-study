package programmers;

/**
 * 프로그래머스 평균 구하기
 * 유형: 수학
 * 난이도: LV1
 */

public class Problem12944 {

    public static void main(String[] args) {
        Solution s = new Solution();

        int arr1[] = {1, 2, 3, 4};
        int arr2[] = {5, 5};

        System.out.println(s.solution(arr1));
        System.out.println(s.solution(arr2));
    }

}
class Solution {

    public double solution(int [] arr) {
        double answer = 0;

        for (int i : arr) {
            answer += i;
        }
        answer = answer / arr.length;

        return answer;
    }
}
