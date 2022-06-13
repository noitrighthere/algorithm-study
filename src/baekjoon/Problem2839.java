package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 백준 2839번 설탕 배달
 * 유형: 그리디
 * 난이도: 실버4
 */

public class Problem2839 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {

        int N = Integer.parseInt(br.readLine());    // 설탕 무게
        int result = 0;

        while (true) {

            if (N % 5 == 0) {
                result = result + (N/5);
                System.out.println(result);
                break;
            }

            N = N - 3;
            result += 1;

            if (N < 0) {
                result = -1;
                System.out.println(result);
                break;
            }
        }
    }
}
