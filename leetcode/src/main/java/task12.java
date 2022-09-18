public class task12 {
    public static int solution(int[] A) {
        int count = 0;
        for (int i=0;i<A.length;++i) {
            int sum = A[i];
            for (int j=i+1;j<A.length;++j) {
                if (sum + A[j] == 0) count++;
                sum += A[j];
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{2,-2,3,0,4,-7}));
    }
}
