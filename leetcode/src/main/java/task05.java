import java.util.*;

public class task05 {
    public static String solution(String S) {
        Set<Character> set = new HashSet<>();
        for (Character c : S.toCharArray()) {
            if (set.contains(c)) return c.toString();
            set.add(c);
        }
        return "";
    }

    public static void main(String[] args) {
        System.out.println(solution(""));
    }
}
