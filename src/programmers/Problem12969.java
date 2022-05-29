package programmers;

import java.util.Scanner;

/**
 * 프로그래머스 직사각형 별찍기
 * 유형: 배열
 * 난이도: LV1
 */

public class Problem12969 {
}

class Solution12969 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        for (int i = 0; i < b; i++) {
            for (int j = 0; j < a; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}