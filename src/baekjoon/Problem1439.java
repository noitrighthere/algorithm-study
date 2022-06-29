package baekjoon;

import java.io.*;
import java.util.*;
import java.lang.*;

/**
 * 백준 1439 뒤집기
 * 유형: 그리디
 * 난이도: 실버5
 */

public class Problem1439 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        StringTokenizer st1 = new StringTokenizer(S, "1");
        StringTokenizer st2 = new StringTokenizer(S, "0");
        System.out.println(Math.min(st1.countTokens(), st2.countTokens()));
        br.close();
    }
}
