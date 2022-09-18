public class task04 {

    public static int solution(int[] A) {
        if (isPleasing(A)) return 0;

        int count = 0;
        int length = A.length;
        for (int i=0;i<length;i++) {
            int[] B = new int[length-1];
            for(int j=0,k=0;j<length;j++) {
                if (i==j) continue;
                B[k] = A[j];
                k++;
            }
            if (isPleasing(B)) count++;
        }
        return count > 0 ? count : -1;
    }

    public static boolean isPleasing(int[] B) {
        for (int i =1;i<B.length-1;i++) {
            if ((B[i]> B[i-1] && B[i] > B[i+1]) || (B[i] < B[i-1] && B[i] < B[i+1])) {
                continue;
            }
            return false;
        }
        return true;
    }

    public static void main(String[] args){
        int A1[] = new int[]{3,4,5,3,7};
        int A2[] = new int[]{1,2,3,4};
        int A3[] = new int[]{1,3,1,2};
        System.out.println(solution(A1));
        System.out.println(solution(A2));
        System.out.println(solution(A3));
    }
}
