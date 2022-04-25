package baekjoon;

/**
 * 백준 10814 나이순 정렬
 * 유형: 정렬
 * 난이도: 실버5
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Problem10814 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        String arr[][] = new String[N][3];

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            String temp[] = s.split(" ");
            arr[i][0] = temp[0];    // 나이
            arr[i][1] = temp[1];    // 이름
            arr[i][2] = Integer.toString(i);    // 가입 순서
        }

        Arrays.sort(arr, (a, b) -> {
            if (a[0] == b[0]) {
                return a[2].compareTo(b[2]);
            } else {
                return Integer.parseInt(a[0]) - Integer.parseInt(b[0]);
            }
        });

        for (int i = 0; i < N; i++) {
            System.out.println(arr[i][0] + " " + arr[i][1]);
        }
    }
}
