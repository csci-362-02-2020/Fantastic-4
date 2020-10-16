
public class testCase2 {
    public static void main(String[] args) {

        // Instantiate the Binomial Distribution Utility class
        BinomialDistributionUtil BinomialDistributionUtil = new BinomialDistributionUtil();

        // Test 2: Normal numerical value in range
        int testTwo = Integer.parseInt(args[0]);
        
        // Run the actual method we are testing
        double value = BinomialDistributionUtil.lnFactorial(testTwo);

        // Print test number
        System.out.println("Test Two:");
        System.out.println("ln(" + testTwo + "!): " + value);

        // Print out test result
        double testOracle = Double.parseDouble(args[1]);

        // Test passed
        if (value == testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Test one passed!");
        }
        // Test failed
        else if (value != testOracle) {
            System.out.println("Oracle: " + testOracle);
            System.out.println("Test one failed...");
        }
        // Test ERROR
        else {
            System.out.println("Test one ERROR");
        }
    }
}