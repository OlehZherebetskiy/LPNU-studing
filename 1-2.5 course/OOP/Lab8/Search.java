package ch.makery.address;

import java.util.ArrayList;
import java.util.List;

import ch.makery.address.model.Domain;

public class Search {
	
	private static List<Domain> con =new ArrayList<Domain>();
	private static String name;

	public static void setname(String name)
	{
		Search.name=name;
	}
	public static void setcon(List<Domain> con)
	{
		Search.con.clear();
		Search.con.addAll(con);
	}
	public static void search_max() throws InterruptedException
	{
		List<Domain> c =new ArrayList<Domain>();
		c.addAll(con);
		
		c.sort(null);
		String s = c.get(0).getName();
		
		//Thread.sleep(1000);
		System.out.println("\"Max\" name is:" +s);
		return;
	}
	public static void search_min() throws InterruptedException
	{
		List<Domain> c1 =new ArrayList<Domain>();
		c1.addAll(con);
		c1.sort(null);
		
		String s = c1.get(c1.size()-1).getName();
		
		//Thread.sleep(1000);
		System.out.println("\"Min\" name is:" +s);
		
	}
	public static void search() throws InterruptedException
	{
		List<Domain> c =new ArrayList<Domain>();
		c.addAll(con);
		int i=0;
		
		for(Domain d : c)
		{ i++;
			
			if(d.getName().equals(name))
			{
			
				System.out.println("This("+name+") was found at plase: "+i);
				return;
			}
		}
		System.out.println("This("+name+") was not found  ");
		
	}
}
