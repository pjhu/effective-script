import java.util.*;
import java.util.stream.*;

public class task07 {
    public static boolean solution(int[] A, int[] P, int B, int E) {
        List<int[]> ranges = new ArrayList<>();
        int length = A.length;
        for (int i=0;i<length;i++){
            int[] range = new int[]{P[i]-A[i], P[i]+A[i]};
            ranges.add(range);
        }
        long count = merge(ranges).stream()
                .filter(e -> (e[0]<=B && e[1]>=E))
                .count();
        return count > 0;
    }

    public static List<int[]> merge(List<int[]> ranges) {
        ranges.sort(Comparator.comparingInt(pre -> pre[0]));
        List<int[]> merges = new ArrayList<>();
        for (int[] range : ranges) {
            int left = range[0];
            int right = range[1];
            if (merges.size() == 0 || merges.get(merges.size() - 1)[1] < left) {
                merges.add(new int[]{left, right});
            } else {
                merges.get(merges.size() - 1)[1] = Math.max(merges.get(merges.size() - 1)[1], right);
            }
        }
        return merges;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{2,1}, new int[] {5,1},3,6));
        System.out.println(solution(new int[]{2,1}, new int[] {5,1},2,6));
        System.out.println(solution(new int[]{1,4,2}, new int[] {10,4,7},11,1));
        System.out.println(solution(new int[]{5,5,1}, new int[] {3,3,6},4,8));
    }
}
