import java.util.ArrayList;
import java.util.List;

public class task11 {
    public static int solution (String s) {
        char[] chars = s.toCharArray();
        char pre = chars[0];
        int count = 0;
        int maxLength = 0;
        List<Integer> list = new ArrayList<>();
        for (char aChar : chars) {
            if (aChar == pre) {
                ++count;
            } else {
                if (maxLength < count) maxLength = count;
                list.add(count);
                pre = aChar;
                count = 1;
            }
        }
        list.add(count);

        int finalMaxLength = maxLength;
        if (list.stream().noneMatch(item -> finalMaxLength != item)) return 0;
        return list.stream()
                .map(e -> (finalMaxLength - e))
                .reduce(0, Integer::sum);
    }

    public static void main(String[] args) {
        System.out.println(solution("aabbba"));
        System.out.println(solution("aabbaa"));
    }
}
