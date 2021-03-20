package ua.lpnuai.zherebetskiy04;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Domain implements Comparable<Domain> {

	
	
	private String name;
    private String unit;
    private String number;
    private String unit_price;
    private String receipt_d;
    private ArrayList<String> about = new ArrayList<String>();
    private Pattern p;
    private	Matcher mn;
    
 //   Pattern p = Pattern.compile("a");
 //   Matcher m = p.matcher(".");
    //[]\^$.|?*+()
    // \\Q...\\E
    //^ otrezanie
    
    /*Крокодил
    шт
    12.2
    5
    12.12.2001
    Колір:зелений
    */
    public  Domain(int i, boolean fast, boolean regex) throws IOException {
    	 {
    		 				String s;
    		 				Scanner in =new Scanner(System.in);
//////////////////////////////////////////////////////////////////////////////////////////////////////////////    	
    	if(!fast)
    		System.out.print("Name(A-Z + a-z):");
    	s = in.nextLine();
    	
    	if(regex)
    		while(!this.setName(s)) {  
    			System.out.println("Invalid format - \t - try again : \n");
    			s = in.nextLine();
    		}	
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////    		
    	if(!fast)
    		System.out.print("Unit(a-z):");
    	s = in.nextLine();
    	
    	if(regex)
    		while(!this.setUnit(s)) {  
    			System.out.println("Invalid format - \t - try again : \n");
    			s = in.nextLine();
    		}	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    	if(!fast)    
    		System.out.print("Unit price(xx.xx):");
s = in.nextLine();
    	
    	if(regex)
    		while(!this.setUnit_price(s)) {  
    			System.out.println("Invalid format - \t - try again : \n");
    			s = in.nextLine();
    		}	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    	if(!fast)    
    		 System.out.print("Number(0-9):");
    	s = in.nextLine();
    	
    	if(regex)
    		while(!this.setNumbers(s)) {  
    			System.out.println("Invalid format - \t - try again : \n");
    			s = in.nextLine();
    		}	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////     
    	if(!fast)    
    	System.out.print("Receipt date(mm.dd.yy):");
    	s = in.nextLine();
   	
    	if(regex)
    		while( !this.setReceipt_d(s)) {  
    			System.out.println("Invalid format - \t - try again : \n");
    			s = in.nextLine();
    		}	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////       
        
    	if(!fast)    
    		System.out.print("About(Xxxxx:.....:)");
        	s = in.nextLine();
       	
        	String m = "";
            ArrayList<String> str = new ArrayList<String>();
            while(!m.equals("done"))
            {
        	if(regex)
        		while(! this.setAbout(str)) {  
        			System.out.println("Invalid format - \t - try again : \n");
        			s = in.nextLine();
        		}
        	str.add(s);
        	System.out.println("More goods - add / else - done");
        	m= in.nextLine();
            }
    	 }
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
       
    }
    
    
    public  Domain() throws IOException {
    }
    public Domain(String suy)
    {
    	Random rand = new Random();
    	StringBuffer s = new StringBuffer();
    	
    	////////////////////////////////////////////////////////
    	char C = (char)(65+rand.nextInt(25));
    	s.append(C);
    	int k=1+rand.nextInt(8);
    	for(int i=0;  i<k;  i++)
    	{
    		char c = (char)(97+rand.nextInt(25));
    		s.append(c);
    	}
    	this.setName(s.toString());
    	/////////////////////////////////////////////////////
    	s.delete(0, s.capacity());
    	k=1+rand.nextInt(8);
    	for(int i=0;  i<k;  i++)
    	{
    		char c = (char)(97+rand.nextInt(25));
    		s.append(c);
    	}
    	this.setUnit(s.toString());
    	//////////////////////////////////////////////////////////
    	s.delete(0, s.capacity());
    	s.append((1+rand.nextInt(8)));
    	s.append((rand.nextInt(9)));
    	s.append(".");
    	s.append((rand.nextInt(9)));
    	s.append((rand.nextInt(9)));
    	this.setUnit_price(s.toString());
    	////////////////////////////////////////////////////////////
    	s.delete(0, s.capacity());
    	s.append((1+rand.nextInt(1000)));
    	this.setNumbers(s.toString());
    	///////////////////////////////////////////////////////////
    	s.delete(0, s.capacity());
    	s.append((rand.nextInt(3)));
    	s.append((rand.nextInt(9)));
    	s.append(".");
    	s.append((rand.nextInt(1)));
    	s.append((rand.nextInt(9)));
    	s.append(".");
    	s.append((rand.nextInt(9)));
    	s.append((rand.nextInt(9)));
    	s.append((rand.nextInt(9)));
    	s.append((rand.nextInt(9)));
    	this.setReceipt_d(s.toString());
    	///////////////////////////////////////////////////////////
    	ArrayList<String> a = new ArrayList<String>();
    	s.delete(0, s.capacity());
    	C = (char)(65+rand.nextInt(25));
    	s.append(C);
    	k=1+rand.nextInt(8);
    	for(int i=0;  i<k;  i++)
    	{
    		char c = (char)(97+rand.nextInt(25));
    		s.append(c);
    	}
    	s.append(":");
    	k=1+rand.nextInt(8);
    	for(int i=0;  i<k;  i++)
    	{
    		char c = (char)(97+rand.nextInt(25));
    		s.append(c);
    	}
    	a.add(s.toString());
    	this.setAbout(a);
    }
    
    @Override
    public String toString()
    {
    	String s ="Name:"+this.name+"\nUnit(Odunuza vumiry):"+this.unit+"\nUnit price:"+this.unit_price+"\nNumber:"+this.number+"\nReceipt date:"+this.receipt_d+"\nAbout:"+this.about.toString() ;
    	return s;
    }
   
    
 ////////////////////////////////////////////////////////   
    public String getName() {
        return name;
    }
    public boolean setName(String name) {
    	
    	p= Pattern.compile("\\b([A-Z]|[А-Я])(([a-zA-Z]|[а-яА-Я])+)?\\b");
    	mn = p.matcher(name);
    	
	   	 if(!mn.find())
	   		return false;
    	
        this.name = name;
        return true;
    }
 ////////////////////////////////////////////////////////   
    
    public String getUnit() {
        return unit;
    }
    public boolean setUnit(String unit) {
    	
    	p= Pattern.compile("\\b([a-z]|[а-я])+\\b");
    	mn = p.matcher(unit);
    	
	   	 if(!mn.find())
	   		return false;
    	
        this.unit = unit+"\n";
        return true;
    }
//////////////////////////////////////////////////////
    
    
    
    
    public String getNumber() {
        return number;
    }
    public boolean setNumbers(String number) {
    	 p= Pattern.compile("\\b\\d+\\b");
    	 mn = p.matcher(number);
     	
	   	 if(!mn.find())
	   		return false;
    	
	   	 this.number = number+"\n";
        return true;
       
    }
    
    
    
    
 /////////////////////////////////////////////////////   
    public String getUnit_price() {
        return unit_price;
    }
    public boolean setUnit_price(String unit_price) {
    	p= Pattern.compile("\\b\\d+\\.\\d{1,2}\\b");
    	 
    	 mn = p.matcher(unit_price);
      	
	   	 if(!mn.find())
	   		return false;
    	
	   	this.unit_price = unit_price+"\n";
        return true;
       
        
    }
/////////////////////////////////////////////////
    
    
    
    
    public String getReceipt_d() {
        return receipt_d;
    }
    public boolean setReceipt_d(String receipt_d) {
    	p= Pattern.compile("\\b\\d{2}[./-]\\d{2}[./-]\\d{4}\\b");
    	mn = p.matcher(receipt_d);
      	
	   	 if(!mn.find())
	   		return false;
   	
	   	this.receipt_d = receipt_d+"\n";
       return true;
        
    }
    
    
    
    
/////////////////////////////////////////

    public ArrayList<String> getAbout() {
        return about;
    }
    public boolean setAbout(ArrayList<String> about) {
    	
    	p= Pattern.compile("([A-Z]|[А-Я])([a-z]|[A-Z]|[а-я]|[А-Я])*[::](.*)");
    	for(String s: about) {
    		mn = p.matcher(s);
	   	 	if(!mn.find())
	   	 		return false;
	   	 	s+="\n";
    	}
    		
  	
	   	 this.about =about;
      return true;
       
    }
    
    
//////////////////////////////////////////////


	@Override
	public int compareTo(Domain o) {
		
		try {
			Thread.sleep(10);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		if(this.getName().charAt(0) > o.getName().charAt(0) )
			return 0;
			
		if(this.getName().charAt(0) == o.getName().charAt(0) )
		{
			if(this.getName().length()>1 && o.getName().length()>1) {
				if(this.getName().charAt(1) > o.getName().charAt(1) )
					return 0;
				
				if(this.getName().charAt(1) == o.getName().charAt(1) )
				{
					
					
					if(this.getName().length()>2 && o.getName().length()>2) {
					if(this.getName().charAt(2) > o.getName().charAt(2) )
						return 0;
						
				
							
						
					
						
						
					if(this.getName().charAt(2) <= o.getName().charAt(2) )
					{
						return -1;
					}	}else return -1;
				}
					
				
			
				
				
				if(this.getName().charAt(1) < o.getName().charAt(1) )
				{
					return -1;
				}
			}
			else return -1;
		}
				
			
		
			
			
		if(this.getName().charAt(0) < o.getName().charAt(0) )
		{
			return -1;
		}
		return -1;	
				
		
			
	}
}
