package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 백준 1026번 보물
 * 유형: 정렬
 * 난이도: 실버4
 */

public class Problem1026 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] A = new int[n];
        int[] B = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        StringTokenizer stk = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(stk.nextToken());
        }

        Arrays.sort(A);
        Arrays.sort(B);

        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += A[i] * B[n-1-i];
        }

        System.out.print(sum);
    }
}
