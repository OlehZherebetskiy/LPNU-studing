package ua.lpnuai.zherebetskiy04;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public  class Regex  {

	public static boolean check (Domain d)
    {
    	Pattern p;
    	Matcher mn;
    	
    	
    	p= Pattern.compile("\\b([A-Z]|[�-�])(([a-zA-Z]|[�-��-�])+)?\\b");
    	 mn = p.matcher(d.getName());
    	 if(!mn.find()) return false;
    	 p= Pattern.compile("\\b\\d+\\b");
    	 if(d.getNumber()!=null)
    	 {
    	 mn = p.matcher(d.getNumber());
    	 if(!mn.find()) return false;
    	 p= Pattern.compile("\\b[0-1]\\d[./-][0-3]\\d[./-]\\[0-2]d{3}\\b");
    	 }
    	 if(d.getReceipt_d()!=null)
    	 mn = p.matcher(d.getReceipt_d());
    	 if(!mn.find()) return false;
    	 p= Pattern.compile("\\b([a-z]|[�-�])+\\b");
    	 if(d.getUnit()!=null)
    	 mn = p.matcher(d.getUnit());
    	 if(!mn.find()) return false;
    	 p= Pattern.compile("\\b\\d+\\.\\d{1,2}\\b");
    	 if(d.getUnit_price()!=null)
    	 mn = p.matcher(d.getUnit_price());
    	 if(!mn.find()) return false;
    	 /*p= Pattern.compile("([A-Z]|[�-�])([a-z]|[A-Z]|[�-�]|[�-�])+:(.+)");
    	 for(String s : this.about)
    	 {
    		 mn = p.matcher(s);
    		 if(!mn.find()) return false;
    	 }*/
    	return true;
    }
	
	public static boolean checkName (Domain d)
    {
		Pattern p;
    	Matcher mn;
		p= Pattern.compile("\\b([A-Z]|[�-�])(([a-zA-Z]|[�-��-�])+)?\\b");
   	 mn = p.matcher(d.getName());
   	 if(!mn.find()) return false;
   	 return true;
    }
	
	
}

