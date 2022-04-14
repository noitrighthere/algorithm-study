package baekjoon;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

/**
 * 백준 2750번 수 정렬하기
 * 유형: 정렬
 * 난이도: 브론즈1
 */

public class Problem2750 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        ArrayList<Integer> list = new ArrayList<Integer>();

        for (int i = 0; i < N; i++) {
            list.add(sc.nextInt());
        }

        list.sort(Comparator.naturalOrder());

        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

        sc.close();
    }
}
