import java.util.*; 
import java.util.function.Supplier; 

public class TestMethod {
    public static void main(String[] args) {

        List<Double> Xlist = new ArrayList<Double>();
        Xlist.add(new Double(5) );
        Xlist.add(new Double(4) );

        List<Double> Ylist = new ArrayList<Double>();
        Ylist.add(new Double(17) );
        Ylist.add(new Double(19) );
        
        
        // slope is -4

        // Instantiate the Binomial Distribution Utility class
        LinearLeastSquaresFit LinearLeastSquaresFitOBJ = new LinearLeastSquaresFit(Xlist, Ylist);

        double slope = LinearLeastSquaresFitOBJ.calculateSlope(Xlist, Ylist);

        System.out.println(slope);

    }
}