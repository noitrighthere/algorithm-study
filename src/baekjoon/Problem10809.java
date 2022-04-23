package baekjoon;

/**
 * 백준 10809번 알바펫 찾기
 * 유형: 문자열
 * 난이도: 브론즈2
 */

import java.util.Scanner;

public class Problem10809 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int [] arr = new int[26];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = -1;
        }

        String s = sc.nextLine();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (arr[ch - 'a'] == -1) {
                arr[ch - 'a'] = i;
            }
        }

        for (int i : arr) {
            System.out.print(i + " ");
        }

    }
}
