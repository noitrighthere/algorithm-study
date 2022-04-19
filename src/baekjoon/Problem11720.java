package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 백준 11720 숫자의 합
 * 유형: 문자열
 * 난이도: 브론즈2
 */

public class Problem11720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();

        int sum = 0;

        for (byte value : br.readLine().getBytes()) {
            sum += (value - '0');
        }

        System.out.println(sum);
    }
}
