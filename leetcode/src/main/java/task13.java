import java.util.ArrayList;
import java.util.List;

public class task13 {
    public static int solution(int[] A){
        int pos = 0;
        for (int i=0;i<A.length-1;++i) {
            if (A[i] != A[i+1]) {
                ++pos;
                continue;
            }
            break;
        }
        if (pos == A.length) return 0;

        int pre = 1 - A[0];
        int countFirst = 1;
        for (int i=1;i<A.length;++i) {
            if (pre == A[i]) {
                pre = 1 - A[i];
                ++countFirst;
            } else {
                pre = A[i];
            }
        }
        int countSecond = 0;
        pre = A[0];
        for (int i=1;i<A.length;++i) {
            if (pre == A[i]) {
                pre = 1 - A[i];
                ++countSecond;
            } else {
                pre = A[i];
            }
        }
        return Math.min(countFirst, countSecond);
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1,0,1,0,1,1}));
        System.out.println(solution(new int[]{1,1,0,1,1}));
        System.out.println(solution(new int[]{0,1,0}));
        System.out.println(solution(new int[]{0,1,1,0}));
    }
}
