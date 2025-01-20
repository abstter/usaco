/* Abhi Avasarala
USACO Fence Painting
1/19
 */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new FileReader("FencePainting/src/paint.in"));
        PrintWriter pw = new PrintWriter("FencePainting/src/paint.out");

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();

        if (b < c || d < a) {
            pw.println((b - a) + (d - c));
        }
        else if (a <= c && b >= d) {
            pw.println(b - a);
        }
        else if (c <= a && d >= b) {
            pw.println(d - c);
        }
        else if (a == c && b == d) {
            pw.println(d - a);
        }
        else {
            int start, end;
            if (a < c) {
                start = a;
            } else {
                start = c;
            }
            if (b > d) {
                end = b;
            } else {
                end = d;
            }
            pw.println(end - start);
        }

        sc.close();
        pw.close();
    }
}
