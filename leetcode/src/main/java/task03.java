import java.util.HashMap;
import java.util.Map;

public class task03 {

    public static boolean solution(int N, int[] A, int[] B) {
        int m = A.length;
        int[][] AB = new int[m][m];
        for (int i=0;i<m;i++){
            AB[A[i]][B[i]] = 1;
            AB[B[i]][A[i]] = 1;
        }
        for (int i=1;i<N;i++)  {
            if (AB[i][i+1] == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[] A = {1,2,4,4,3};
        int[] B = {2,3,1,3,1};
        System.out.println(solution(4,A,B));
    }
}
