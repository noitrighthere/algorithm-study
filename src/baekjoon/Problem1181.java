package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 백준 1181번 단어 정렬
 * 유형: 배열
 * 난이도: 실버5
 */

public class Problem1181 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        HashSet<String> set = new HashSet<String>();

        // 값 입력
        for (int i = 0; i < N; i++) {
            set.add(br.readLine());
        }

        // 리스트 변환
        ArrayList<String> list = new ArrayList<String>(set);

        // Comparator 클래스를 통해여 custom 정렬
        Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String v1, String v2) {
                if (v1.length() > v2.length()) {
                    return 1;
                } else if (v1.length() < v2.length()) {
                    return -1;
                } else {
                    return v1.compareTo(v2);
                }
            }
        });

        for (String s : list) {
            System.out.println(s);
        }
    }
}
