import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

public class task18 {
    public static int[] solution(int[] A, int F, int M){
        int total = (A.length+F) * M;
        List<Integer> list = Arrays.stream(A).boxed().collect(Collectors.toList());
        int sum = list.stream().reduce(0, Integer::sum);

        int forgot = total - sum;
        if (forgot > 6*F || forgot < F) return new int[]{0};
        int[] result = new int[F];
        for (int i=1;i<=forgot;++i) {
            result[i%F] += 1;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{3, 2, 4, 3}, 2, 4)));
        System.out.println(Arrays.toString(solution(new int[]{1, 5, 6}, 4, 3)));
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3, 4}, 4, 6)));
        System.out.println(Arrays.toString(solution(new int[]{6, 1}, 1, 1)));
    }
}
