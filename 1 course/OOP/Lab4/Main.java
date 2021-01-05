package ua.lpnuai.zherebetskiy04;

import java.io.IOException;
import java.util.*;


class MyThread extends Thread
{
	
	int i =0;
	public void geti(int i)
	{
		this.i=i;
	}
	
	@SuppressWarnings("deprecation")
	@Override
	public void run()
	{ 
		
		if(i==0)
		{
			try {
				
				Search.search_max();				
			
				
		
			} catch (InterruptedException e) {
			
				e.printStackTrace();
			}
		}
		if(i==1)
		{
			try {
				Search.search_min();				
				
			
			} catch (InterruptedException e) {
				
				e.printStackTrace();
			}
		}
		if(i==2)
		{
			try {
				Search.search();				
				
		
			} catch (InterruptedException e) {
				
				e.printStackTrace();
			}
		}
		
		this.stop();
		
	}
	
	
	
}


public class Main {

	@SuppressWarnings("deprecation")
	public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
		
		boolean point = false;
		long timelimit=0;
		String searchString = " ";
		
		//Collection<Domain> con = new ArrayList<Domain>();
		List<Domain> con = new ArrayList<Domain>();
		
		
		File_work<Domain> File_work = new File_work<Domain>();
		if (args.length > 0)  point = Menu.prehelp(args[0]) ;
		Menu.help();
		Scanner sc = new Scanner(System.in);
		Domain element = new Domain();
		while (true) {
		switch (Menu.comscanwork(point))
		{
		case(11):  case( 100):
			
		if(point) { element=File_work.ReadXML(File_work.path.toString()+"\\auto",0).get(0);
			if(Regex.check(element))
			{
   	   
				element.toString();
			}
			else
			{
			 
				System.out.println("Invalid data #" +"\t From \t");
				
				element=null;
				return;
			}}
		else
			element = new Domain(1,false,true);
			break;
			
		case(16):  
			
			
				element = new Domain(1,true,true);
				con.add(element);
			break;
			
		case(1): case( 101)://add
			
			con.add(element);
			break;
		case(2): case( 102)://out
			for(Object str : con )
	    	{
	    		System.out.println(str);
	    		System.out.println(".\n.\n.\n.\n");
	    	}
			break;
		case (3)://contains
			Domain elem = new Domain(1,false,true);
			con.contains(elem);
			break;
		case(4)://remove
			Domain text = new Domain(1,false,true);
			con.remove(text);
			break;
		case(5)://clean
			con.clear();
			break;
		case(6): case( 103):
			String n;
		ArrayList<Domain> ar =new ArrayList<Domain>();
		if(point)
		{
			n="auto1";
			
			ar.add(element);
			
		}
		else {
			System.out.print("Name of file:");
			sc.nextLine();
			 n = sc.nextLine();
		
			
		    	
		        
			Scanner scr = new Scanner(System.in);
            String m = "add"; 
            
            while (!m.equals("done")) {
               
                switch (m) {
                    case "add":
                        
                    ar.add(new Domain(1,false,true));
                     
                       break;
                       
                }
                System.out.println("add more info about -'add', else 'done'");
                
                m = scr.nextLine();
            }}
			File_work.WriteXMLE(File_work.path.toString()+"\\"+n, ar);
			break;
		case(7): case( 104):
			String n1;
			if(point)
				n1="auto1";
			else {
			System.out.print("Name of file:");
			 n1 = sc.nextLine();
			}
			ArrayList<Domain> arr = File_work.ReadXML(File_work.path.toString()+"\\"+n1,1);
			int ik=1 ,ki=1;
			 for(Domain el : arr)
	           {
				 if(Regex.check(el))
				 {
	        	   con.add(el);
	        	   el.toString();
				 }
				 else
				 {
					 
					 System.out.println("Invalid data #"+ik +"\t From \t"+ ki);
					 ik++;
				 }
				 ki++;
	           }
			break;
		case(8):
			
			File_work.WriteF(File_work.path.toString(),element.toString());
			break;
		case(15):
			
			Collections.sort(con);
			
			break;
		case(9):
			
			File_work.ReadF();
			break;
		case(10):
			System.out.print("Name of file:");
			StringBuffer fpath = new StringBuffer() ;
			fpath.append(sc.nextLine());
			File_work.MoveForvard(fpath);
			break;
		case(12):
			File_work.MoveBack();
			break;
		case(13):
			File_work.Show();
			break;
		case(18):
			timelimit=sc.nextLong();
			break;
		case(19):
			Scanner sc1 = new Scanner(System.in);
			System.out.println("Input searchString:");
			searchString = sc1.nextLine();
		
			break;
			////////////////////////////////////////////////////
		case(20):
			MyThread searchmaxThread = new MyThread();
			MyThread searchminThread = new MyThread();
			MyThread searchThread = new MyThread();
			searchmaxThread.i=0;
			searchminThread.i=1;
			searchThread.i=2;
			Search.setcon(con);
			Search.setname(searchString);
			
			long start = System.currentTimeMillis();
			
			searchmaxThread.start();
			searchminThread.start();
			searchThread.start();
			long finish;
			while(true)
			{
				if(!searchmaxThread.isAlive() &&!searchminThread.isAlive() &&!searchThread.isAlive() )
				{
					finish = System.currentTimeMillis();
					break;
				}
				if(System.currentTimeMillis()-start>=timelimit)
				{
					 finish = System.currentTimeMillis();
					searchmaxThread.stop();
					searchminThread.stop();
					searchThread.stop();
					System.out.println("ERROR: TIME LIMIT !!!!");
					break;
					
				}
				
					
			}
			
			
			
			
			
			System.out.println("Time(millis):\t"+(finish-start));
			
			break;
			/////////////////////////////////////////////////////
		case(21):
			
			long start1 = System.currentTimeMillis();
			Search.setcon(con);
			Search.setname(searchString);
			Search.search_max();
			Search.search_min();
			Search.search();
			
			long finish1 = System.currentTimeMillis();
			System.out.println("Time(millis):\t"+(finish1-start1));
			break;
		case(22):
			System.out.println("Amount:\t");
			int k =sc.nextInt();
			for(int i=0 ;i<k;i++) {
			Domain d = new Domain("rand");
			con.add(d);
			}
			break;
		case(0): case( 105):
			System.out.println( ".\n\t\t\t\t\t\t\t\tGoooodbye! \t" );
			sc.close();
			System.exit(0);
			break ;
		default:
			break;
		}
		}
	}

}
