package colaboratordesignpatter;

import java.beans.Customizer;
import java.time.LocalDate;
import static colaboratordesignpatter.CombinatorInterface.*;

/**
 *
 * @author Ashutosh Kedar
 */
public class ColaboratorDesignPatter {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Customer newCustomer = new Customer(
            "ashutosh@gmail.com",
            "9133683733",
            LocalDate.of(1999,2,15)
            );
        
        
        Result custResult = isEmailValid()
                  .and(isAdult())
                  .and(isPhoneValid())
                  .apply(newCustomer);
        
            System.out.println(custResult);

    }
    
    
}
