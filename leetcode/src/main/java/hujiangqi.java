import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

public class hujiangqi {
    public static int solution(String S) {
        char[] chars = S.toCharArray();
        int n = S.length();
        int length = 0;
        for (int i=1;i<=n/2;++i) {
            boolean match = true;
            for (int j=i;j<n;++j) {
                if (chars[j] != chars[j-i]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                length = Math.max(length, i);
            }
        }
        return length;
    }

    private static final Map<String, LocalDateTime> expiredKeyMap = new HashMap<>(10);
    private static final Map<String, String> keyMap = new HashMap<>(10);
    public static void putKey(String key, String value, long second) {
        LocalDateTime expiredDate = LocalDateTime.now().plusSeconds(second);
        expiredKeyMap.put(key, expiredDate);
        keyMap.put(key, value);
    }

    private static String getKey(String key) {
        LocalDateTime now = LocalDateTime.now();
        if(!expiredKeyMap.containsKey(key) || now.isAfter(expiredKeyMap.get(key))) {
            expiredKeyMap.remove(key);
            keyMap.remove(key);
            return null;
        }
        return keyMap.get(key);
    }

    public static void main(String[] args) throws InterruptedException {
//        System.out.println(solution("kylinstwkylinstwkyli"));
        putKey("1","1", 5);
        System.out.println(getKey("1"));
        TimeUnit.SECONDS.sleep(5L);
        System.out.println(getKey("1"));
    }
}
