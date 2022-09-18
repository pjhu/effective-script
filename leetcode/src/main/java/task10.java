import java.util.*;
public class task10 {

    public static boolean solution(int[] A, int[] B){
        int length = A.length;
//        Map<Integer, List<Integer>> map = new HashMap<>();
//        for (int i=0;i<length;++i){
//            if (map.get(A[i]) ==  null) {
//                List<Integer> list = new ArrayList<>();
//                list.add(B[i]);
//                map.put(A[i], list);
//            } else {
//              map.get(A[i]).add(B[i]);
//            }
//        }
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=0;i<length;++i){
            if (A[i] == B[i]) continue;
            if(!map.containsKey(A[i])) {
                map.put(A[i], B[i]);
            } else {
                return false;
            }
        }

        int cur = A[0];
        Set<Integer> set = new HashSet<>();
        for (int i=0;i<length;++i){
            cur = map.get(cur);
            set.add(cur);
        }
        return set.size() == length && cur == A[0];
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1,3,2,4}, new int[]{4,1,3,2}));
        System.out.println(solution(new int[]{1,2,3,4}, new int[]{2,1,4,3}));
        System.out.println(solution(new int[]{3,1,2}, new int[]{2,3,1}));
        System.out.println(solution(new int[]{1,2,2,3,3}, new int[]{2,3,3,4,5}));
    }
}
