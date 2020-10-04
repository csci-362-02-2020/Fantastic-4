
public class TestMethod {
    public static void main(String[] args) {

        // Instantiate the Binomial Distribution Utility class
        BinomialDistributionUtil BinomialDistributionUtil = new BinomialDistributionUtil();

        // Test 1: Normal numerical value in range
        int testOne = 3;
        double value = BinomialDistributionUtil.lnFactorial(testOne);
        System.out.println("Test one:");
        System.out.println("ln(" + testOne + "!): " + value);

        // Print out test result
        double testOneOracle = 1.791759469228055;
        if (value == testOneOracle) {
            System.out.println("Expected Result: " + testOneOracle);
            System.out.println("Actual Result: " + value);
            System.out.println("Test one passed!");
        }
        else if (value != testOneOracle) {
            System.out.println("Expected Result: " + testOneOracle);
            System.out.println("Actual Result: " + value);
            System.out.println("Test one failed...");
        }
        else {
            System.out.println("Test one ERROR");
        }
    }
}