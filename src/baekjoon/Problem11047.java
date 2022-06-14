package baekjoon;

import java.util.Scanner;

/**
 * 백준 11047번 동전 0
 * 유형: 그리디
 * 난이도: 실버4
 */

public class Problem11047 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int count = 0;  // 동전 개수(결과값)

        int N = sc.nextInt();
        int K = sc.nextInt();   // 만들어야 할 금액

        int[] coins = new int[N];

        // 동전의 가치를 배열로 다음
        for (int i = 0; i < N; i++) {
            coins[i] = sc.nextInt();
        }

        for (int i = N-1; i >= 0; i--) {

            if (coins[i] <= K) {

                count += (K / coins[i]);
                K = K % coins[i];
            }
        }

        System.out.println(count);
    }
}
