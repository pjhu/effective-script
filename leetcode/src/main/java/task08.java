public class task08 {

    public static int solution(int N){
        if (N==1) return 0;
        int[] d = new int[30];
        int l = 0;
        int p;
        while (N>0) {
            d[l] = N % 2;
            System.out.print(d[l]);
            N /= 2;
            l++;
        }
        for (p=1;p<l;++p) {
            int i;
            boolean ok = true;
            for (i=0;i<l-p;++i) {
                if(d[i] != d[i+p]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                return p;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(solution(1));
    }
}
