// [rectangleStar.java]
// 직사각형 별찍기

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        // 행의 개수
        for (int i=0; i<b; i++){
            // 열의 개수
            for (int j=0; j<a; j++){
                System.out.print("*");
            }
            System.out.println();
        }
        
    }
}