package ua.lpnuai.oop.Zherebetskiy03;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Catalog {

	
	private String name;
    private String unit;
    private String number;
    private String unit_price;
    private String receipt_d;
    private ArrayList<String> about = new ArrayList<String>();
    
    
    public  Catalog(int i) throws IOException {
    	Scanner in =new Scanner(System.in);
    	
    	System.out.print("Name:");
        this.setName(in.nextLine()+"\n");

        System.out.print("Unit(Odunuza vumiry):");
        this.setUnit(in.nextLine()+"\n");
        
         System.out.print("Unit price:");
        this.setUnit_price(in.nextLine()+"\n");
        
        System.out.print("Number:");
        this.setNumbers(in.nextLine()+"\n");
        
        System.out.print("Receipt date:");
        this.setReceipt_d(in.nextLine()+"\n");
        
        System.out.print("About:");
        String m = "";
        ArrayList<String> str = new ArrayList<String>();
        while(!m.equals("done"))
        {
        	str.add(in.nextLine());
        	System.out.println("More goods - add / else - done");
        	m= in.nextLine();
        	
        }
        str.add("\n");
        this.setAbout(str);

       
        
    }
    
    public  Catalog() throws IOException {
    }
    
   
    
 ////////////////////////////////////////////////////////   
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
 ////////////////////////////////////////////////////////   
    
    public String getUnit() {
        return unit;
    }
    public void setUnit(String unit) {
        this.unit = unit;
    }
//////////////////////////////////////////////////////
    
    
    
    
    public String getNumber() {
        return number;
    }
    public void setNumbers(String number) {
        this.number = number;
    }
    
    
    
    
 /////////////////////////////////////////////////////   
    public String getUnit_price() {
        return unit_price;
    }
    public void setUnit_price(String unit_price) {
        this.unit_price = unit_price;
    }
/////////////////////////////////////////////////
    
    
    
    
    public String getReceipt_d() {
        return receipt_d;
    }
    public void setReceipt_d(String receipt_d) {
        this.receipt_d = receipt_d;
    }
    
    
    
    
/////////////////////////////////////////

    public ArrayList<String> getAbout() {
        return about;
    }
    public void setAbout(ArrayList<String> about) {
        this.about =about;
    }
//////////////////////////////////////////////
}
