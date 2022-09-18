public class task01 {
    public static int solution(int[] A) {
        int N = A.length;
        int cost = Integer.MAX_VALUE;
        for (int i=1;i<N-1;i++)
            for (int j = i + 2; j < N - 1; j++)
                cost = Math.min(cost,A[i] + A[j]);
        return cost;
    }

    public static void main(String[] args) {
        int[] A = new int[]{5,2,4,6,3,7};
        System.out.println(solution(A));
    }
}
