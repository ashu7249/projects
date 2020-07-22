/*
 *
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 *
 */
package colaboratordesignpatter;

import colaboratordesignpatter.CombinatorInterface.Result;
import java.time.LocalDate;
import java.util.function.Function;

/**
 *
 * @author Ashutosh Kedar
 *
 */

public interface CombinatorInterface extends Function<Customer,Result>{
    
    static CombinatorInterface isEmailValid(){
        return customer -> {
                   return customer.getEmailID().contains("@") ? Result.SUCCESS : Result.EMAIL_NOT_VALID ;   
        };
    }
    

    static CombinatorInterface isPhoneValid(){
        return customer -> {
            return customer.getMobNO().startsWith("91") ? Result.SUCCESS : Result.PHONE_NOT_VALID;
        };
    }
    

    static CombinatorInterface isAdult(){
        return customer ->{
            return LocalDate.now().getYear() - customer.getDob().getYear() > 18 ? Result.SUCCESS : Result.NOT_ADULT; 
        };
    }
    

    default CombinatorInterface and ( CombinatorInterface next){
    
        return customer ->{
            Result result = this.apply(customer);
            return result.equals(Result.SUCCESS) ? next.apply(customer) : result;
                    
        };
     
 	
    }
  
    
    enum Result{
        SUCCESS,
        EMAIL_NOT_VALID,
        PHONE_NOT_VALID,
        NOT_ADULT
    }
    
}
