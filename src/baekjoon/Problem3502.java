package baekjoon;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * 백준 3052번 나머지
 * 유형: 배열
 * 난이도: 브론즈2
 */

public class Problem3502 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            list.add(sc.nextInt() % 42);
        }

        List<Integer> result = new ArrayList<>();
        for (int a : list) {
            if(!result.contains(a)) {
                result.add(a);
            }
        }

        System.out.println(result.stream().count());

        sc.close();
    }
}
