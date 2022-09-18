public class task02 {
    // https://leetcode.cn/problems/maximum-trailing-zeros-in-a-cornered-path/
    // https://www.geeksforgeeks.org/maximize-trailing-zeros-in-product-from-top-left-to-bottom-right-of-given-matrix/
    public static int solution(int[][] A) {
        int row=A.length,colum=A[0].length;
        int zeros = 0;
        for (int i=0;i<row;i++) {
            for (int j=0;j<colum;j++) {
                int up2,down2,left2,right2,up5,down5,left5,right5;
                up2=down2=left2=right2=up5=down5=left5=right5=0;
                for (int m=0;m<i;m++) {
                    up2 += getFactorNum(A[m][j],2);
                    up5 += getFactorNum(A[m][j],5);
                }
                for (int m=i+1;m<row;m++) {
                    down2 += getFactorNum(A[m][j],2);
                    down5 += getFactorNum(A[m][j],5);
                }
                for (int n=0;n<j;n++) {
                    left2 += getFactorNum(A[i][n],2);
                    left5 += getFactorNum(A[i][n],5);
                }
                for (int n=j+1;n<colum;n++) {
                    right2 += getFactorNum(A[i][n],2);
                    right5 += getFactorNum(A[i][n],5);
                }

                int cur2 = getFactorNum(A[i][j],2);
                int cur5 = getFactorNum(A[i][j],5);
                int ul = Math.min(up2+left2+cur2, up5+left5+cur5);
                int ur = Math.min(up2+right2+cur2, up5+right5+cur5);
                int dl = Math.min(down2+left2+cur2, down5+left5+cur5);
                int dr = Math.min(down2+right2+cur2, down5+right5+cur5);

                int cur = Math.max(ul, ur);
                cur = Math.max(cur, dl);
                cur = Math.max(cur, dr);
                zeros = Math.max(zeros, cur);

//                System.out.println("========"+i+j);
//                System.out.println("zero:"+zeros);
//                if (ul == zeros) {
//                    System.out.println("ul");
//                }
//                if (ur == zeros) {
//                    System.out.println("ur");
//                }
//                if (dl == zeros) {
//                    System.out.println("dl");
//                }
//                if (dr == zeros) {
//                    System.out.println("dr");
//                }
            }
        }
        return zeros;
    }

    public static int getFactorNum(int num, int factor) {
        int k = 0;
        while (num % factor == 0 ) {
            num /= factor;
            k++;
        }
        return k;
    }

    public static void main(String[] args) {
        int[][] A1 = {{10,100,10},{1,10,1}};
        int[][] A2 = {{5,8,3,1},{4,15,12,1},{6,7,10,1},{9,1,2,1}};
        int[][] A3 = {{7500,10,11,12},{6250,13,14,15},{134,17,16,1},{5500,2093,5120,238}};

        System.out.println("===result======");
        System.out.println(solution(A1));
        System.out.println(solution(A2));
        System.out.println(solution(A3));
    }
}
