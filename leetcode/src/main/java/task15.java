import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.stream.*;

public class task15 {
    public static int solution(String S) {
        Map<String, Integer> map = new HashMap<>();
        map.put("Mon",1);
        map.put("Tue",2);
        map.put("Wed",3);
        map.put("Thu",4);
        map.put("Fri",5);
        map.put("Sat",6);
        map.put("Sun",7);

//        List<String> list = Arrays.stream(S.split("\n")).sorted()
//                .map(item -> {
//                    List<>item.split("[ :-]")
//                })
//                .collect(Collectors.toList());

        return 0;
    }

    public static void main(String[] args) throws ParseException {
        int solution = solution("");
        SimpleDateFormat format = new SimpleDateFormat("E");
        Date date = format.parse("Mon 10:00");
        System.out.println(date);
    }
}
