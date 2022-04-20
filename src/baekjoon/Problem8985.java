package baekjoon;

import java.util.Scanner;

/**
 * 백준 8985 OX퀴즈
 * 유형: 문자열
 * 난이도: 브론즈2
 */

public class Problem8985 {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int t = sc.nextInt();

       String str;

       for (int i = 0; i < t; i++) {
           int cnt = 0;
           int sum = 0;

           str = sc.next();

           for (int j = 0; j < str.length(); j++) {
               if (str.charAt(j) == 'O') {
                   cnt++;
                   sum += cnt;
               } else {
                   cnt = 0;
               }
           }
           System.out.println(sum);
       }
    }
}
