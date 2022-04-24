package baekjoon;

/**
 * 백준 1316번 그룹 단어 체커
 * 유형: 문자열
 * 난이도: 실버5
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Problem1316 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        int count = 0;
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            if (check()) {
                count++;
            }
        }
        System.out.print(count);
    }

    public static boolean check() throws IOException {
        boolean[] check = new boolean[26];
        int prev = 0;
        String str = br.readLine();

        for (int i = 0; i < str.length(); i++) {
            int cur = str.charAt(i);

            if (prev != cur) {
                if (!check[cur - 'a']) {
                    check[cur - 'a'] = true;
                    prev = cur;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}
