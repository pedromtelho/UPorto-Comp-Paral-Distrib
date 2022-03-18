import java.util.Scanner;

public class Matrix {

    public static void main(String[] args) {
        int op, lin, col;
        Scanner in = new Scanner(System.in);
        System.out.println("1. Multiplication");
        System.out.println("2. Line Multiplication");
        System.out.println("3. Block Multiplication");
        System.out.print("Selection?: ");
        op = in.nextInt();
        System.out.print("Dimensions: lins=cols ? ");
        lin = in.nextInt();
        col = lin;
        double[][] testMat = createTestMatrixes(lin, col);

        double[] phc = new double[lin * col];
        long timeElapsed = 0;
        switch (op) {
            case 1:
                timeElapsed = onMult(phc, testMat[0], testMat[1], lin, col);
                break;
            case 2:
                timeElapsed = onMultLine(phc, testMat[0], testMat[1], lin, col);
                break;
            case 3:
                System.out.print("Block Size? ");
                onMultBlock(phc, testMat[0], testMat[1], lin, col, in.nextInt());
                break;
            default:
                System.out.println("Invalid select");
                in.close();
                return;
        }
        System.out.println("Time: " + (double) timeElapsed / 1000000000 + " seconds");
        displayFirstTen(phc, col);

        in.close();
    }

    static long onMult(double[] phc, double[] pha, double[] phb, int m_ar, int m_br) {
        long start = System.nanoTime();
        for (int i = 0; i < m_ar; i++) {
            for (int j = 0; j < m_br; j++) {
                int temp = 0;
                for (int k = 0; k < m_ar; k++) {
                    temp += pha[i * m_ar + k] * phb[k * m_br + j];
                }
                phc[i * m_ar + j] = temp;
            }
        }
        long finish = System.nanoTime();
        return finish - start;
    }

    static long onMultLine(double[] phc, double[] pha, double[] phb, int m_ar, int m_br) {
        long start = System.nanoTime();
        for (int i = 0; i < m_ar; i++) {
            for (int k = 0; k < m_ar; k++) {
                for (int j = 0; j < m_br; j++) {
                    phc[i * m_ar + j] += pha[i * m_ar + k] * phb[k * m_br + j];
                }
            }
        }
        long finish = System.nanoTime();
        return finish - start;
    }

    static long onMultBlock(double[] phc, double[] pha, double[] phb, int m_ar, int m_br, int bkSize) {
        long start = System.nanoTime();


        for (int bi = 0; bi < m_ar; bi += bkSize) {
            for (int bj = 0; bj < m_br; bj += bkSize) {
                for (int bk = 0; bk < m_ar; bk += bkSize) {
                    for (int i = 0; i < bkSize; i++) {
                        for (int j = 0; j < bkSize; j++) {
                            for (int k = 0; k < bkSize; k++) {
                                phc[(bi + i) * m_ar + bj + j] += pha[(bi + i) * m_ar + bk + k]
                                        * phb[(bk + k) * m_ar + bj + j];
                            }
                        }
                    }
                }
            }
        }

        long finish = System.nanoTime();
        return finish - start;
    }

    static double[][] createTestMatrixes(int m_ar, int m_br) {
        double[] pha = new double[m_ar * m_ar];
        double[] phb = new double[m_br * m_br];

        for (int i = 0; i < m_ar; i++)
            for (int j = 0; j < m_ar; j++)
                pha[i * m_ar + j] = (double) 1.0;

        for (int i = 0; i < m_br; i++)
            for (int j = 0; j < m_br; j++)
                phb[i * m_br + j] = (double) (i + 1);

        return new double[][] { pha, phb };
    }

    static void displayFirstTen(double[] phc, int m_br) {
        // display 10 elements of the result matrix tto verify correctness
        System.out.println("Result Matrix:");

        for (int i = 0; i < 1; i++) {
            for (int j = 0; j < Math.min(10, m_br); j++)
                System.out.print(phc[j] + " ");
        }
        System.out.println();
    }
}
