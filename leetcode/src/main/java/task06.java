import java.util.*;
import java.util.stream.*;
public class task06 {
    public static class UserStats {
        public int count() {
            return 0;
        }

        public Optional<Long> getUserCount() {
            return Optional.of(1L);
        }
    }
    static Map<Long, Long> solution(Map<String, UserStats>... visits ){
        Map<Long, Long> ans = new HashMap<>();
        if (visits == null) return ans;
        for (Map<String, UserStats> user : visits) {
            if (user == null || user.isEmpty()) continue;
            for (String key : user.keySet()) {
                UserStats userStats = user.get(key);

                Optional<Long> l = userStats.getUserCount();
                if (l.isEmpty()) continue;
                if (!isNumeric(key)) continue;
                Long id = Long.valueOf(key);
                Long count = ans.getOrDefault(id, 0L);
                ans.put(id, count+l.get());
            }
        }
        return ans;
    }

    public static boolean isNumeric(String s) {
        for (char c : s.toCharArray()) {
            if (c < '0' || c>'9') return false;
        }
        return true;
    }
}


