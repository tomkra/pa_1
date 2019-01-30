import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int size = 3;
        Random rand = new Random();
        double[][] mat = new double[][] { {1,3,-2},{4,2,8},{-3,1,0} };
        //double[][] mat = new double[][] { {1,2,4},{3,8,14},{2,6,13} };
        double[][] randmat = new double[size][size];
        for(int i=0; i<size; i++) {
            for(int j=0; j<size; j++) {
                randmat[i][j] = rand.nextInt();
            }
        }

        LuDecomposition lu = new LuDecomposition(mat, size);
        lu.decompose();
    }
}
