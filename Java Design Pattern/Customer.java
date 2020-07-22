/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package colaboratordesignpatter;

import java.time.LocalDate;
/**
 *
 * @author Ashutosh Kedar
 */
public class Customer {
    private String emailID;
    private String mobNO;
     private LocalDate dob;

    public Customer(String emailID, String mobNO, LocalDate dob) {
        this.emailID = emailID;
        this.mobNO = mobNO;
        this.dob = dob;
    }
    public void setEmailID(String emailID) {
        this.emailID = emailID;
    }

    public void setMobNO(String mobNO) {
        this.mobNO = mobNO;
    }

    public void setDob(LocalDate dob) {
        this.dob = dob;
    }

    public String getEmailID() {
        return emailID;
    }

    public String getMobNO() {
        return mobNO;
    }

    public LocalDate getDob() {
        return dob;
    }        
}
