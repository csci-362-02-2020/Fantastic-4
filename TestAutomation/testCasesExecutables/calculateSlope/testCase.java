import java.util.*; 
import java.util.function.Supplier; 

public class testCase {
    public static void main(String[] args) {

        // Assign values from input
        Double x1 = Double.parseDouble(args[0]);
        Double y1 = Double.parseDouble(args[1]);
        Double x2 = Double.parseDouble(args[2]);
        Double y2 = Double.parseDouble(args[3]);

        // Print out test result
        double testOracle = Double.parseDouble(args[4]);
        
        List<Double> Xlist = new ArrayList<Double>();
        Xlist.add(new Double(x1));
        Xlist.add(new Double(x2));

        List<Double> Ylist = new ArrayList<Double>();
        Ylist.add(new Double(y1));
        Ylist.add(new Double(y2));

        // Instantiate the Binomial Distribution Utility class
        LinearLeastSquaresFit LinearLeastSquaresFitOBJ = new LinearLeastSquaresFit(Xlist, Ylist);

        double slope = LinearLeastSquaresFitOBJ.calculateSlope(Xlist, Ylist);

        // Print test number
        System.out.println("Test:");
        System.out.printf("Calculate slope bettween (%f, %f) and (%f, %f)\n", x1, y1, x2, y2);

        System.out.println("Result: " + slope);

        // Test passed
        if (slope == testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Test one passed!");
        }
        // Test failed
        else if (slope != testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Test one failed...");
        }
        // Test ERROR
        else {
            System.out.println("Test one ERROR");
        }
    }
}