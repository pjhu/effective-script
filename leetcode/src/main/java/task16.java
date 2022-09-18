import java.util.*;

public class task16 {
    public static int solution(String str) {
        for(int k=1;k<=str.length();k++){
            for(int i=0;i<str.length()-k+1;i++){
                Set<Character> lowerSet = new HashSet<>();
                Set<Character> upperSet = new HashSet<>();
                String temp = str.substring(i,i+k);
                char[] tempCharArr = temp.toCharArray();
                for(char ch : tempCharArr){
                    if(Character.isLowerCase(ch))
                        lowerSet.add(ch);
                    else
                        upperSet.add(ch);
                }
                if(containsAllElements(lowerSet, upperSet)
                        && containsAllElements(upperSet, lowerSet)){
                    return temp.length();
                }
            }
        }
        return -1;
    }

    static boolean containsAllElements(Set<Character> first, Set<Character> second){
        Set<Character> lower1 = new HashSet<>();
        Set<Character> lower2 = new HashSet<>();
        first.forEach((e) -> lower1.add(Character.toLowerCase(e)));
        second.forEach((e) -> lower2.add(Character.toLowerCase(e)));
        return lower1.containsAll(lower2);
    }

    public static void main(String[] args) {
        System.out.println(solution("azABaabza"));
        System.out.println(solution("TacoCat"));
        System.out.println(solution("AcZCbaBz"));
        System.out.println(solution("aafsfefefsfsefsefesfef"));
        System.out.println(solution("CATattac"));
        System.out.println(solution("Madam"));
    }
}
