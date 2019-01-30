import java.util.stream.IntStream;

public class LuDecomposition {
    private int size;
    private double[][] matrix;

    public LuDecomposition(double[][] matrix, int size) {
        this.matrix = matrix;
        this.size = size;
    }

    public void printMatrix(double[][] matrix) {
        for(int i=0; i<size; i++) {
            for(int j=0; j<size; j++) {
                System.out.printf("%.2f   ", matrix[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }

    public void decompose() {
        double[][] upper = new double[this.size][this.size];
        double[][] lower = new double[this.size][this.size];

        for(int i=0; i<size; i++) {
            for(int j=0; j<size; j++) {
                upper[i][j] = 0.0;
                lower[i][j] = 0.0;
            }
        } 

        long start = System.nanoTime();

        IntStream.range(0, size).parallel().forEach(i -> {
            // U matrix
            for (int k = i; k < size; k++) {
                double sum = 0.0;
                for (int j = 0; j < i; j++) {
                    sum += (lower[i][j] * upper[j][k]);
                }
                upper[i][k] = matrix[i][k] - sum;
            }
            // L matrix
            for (int k = i; k < size; k++) {
                if (i == k) {
                    lower[i][i] = 1;
                } else {
                    double sum = 0.0;
                    for (int j = 0; j < i; j++) {
                        sum += (lower[k][j] * upper[j][i]);
                    }
                    lower[k][i] = ((matrix[k][i] - sum) / upper[i][i]);
                }
            }
        });

        long end = System.nanoTime();

        //printMatrix(matrix);
        //printMatrix(lower);
        //printMatrix(upper);
        System.out.println("LU decomposition duration(seconds): " + (end - start) / 1000000000.0);
    }

}
