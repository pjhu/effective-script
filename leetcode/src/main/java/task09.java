public class task09 {

    public static int solution(int[] A){
        int length = A.length;
        for (int i=1;i<length;++i){
            if (A[i] > A[i-1]) return i+1;
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{5,-2,3,8,6}));
        System.out.println(solution(new int[]{-5,-5,-5,-42,6,12}));
    }
}
