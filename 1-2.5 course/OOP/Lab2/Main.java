package ua.lpnuai.oop.Zherebetskiy02;

import java.io.IOException;



public class Main {

	public static void main(String[] args) throws IOException, ClassNotFoundException {
		boolean point = false;
		Container con = new Container();
		if (args.length > 0)  point = Menu.prehelp(args[0]) ;
		
		String str_text = new String();
		String str_list = new String();
		int word = 0;
		
		
		while (true) {
		switch (Menu.comscanwork())
		{
		case(1):
			str_text = List.scan_text();
			str_list = List.scan_list();
			word = List.scan_word();
			break;
		case(2):
			List.Out_d(str_text, str_list, word);
			break ;
		case(3):
			str_text = List.str_work(str_text, str_list, word,point);
		if (point==true) List.Out_d(str_text, str_list, word);
			break ;
		case(4):
			System.out.println("\nText:\t"+str_text);
			break ;
		case(5):
			con.add(str_text, str_list, word);
			break ;
		case(6):
		
			SER_DE.serre(con.toString());
		
		break ;
		case(11):
			
			con.clear();
		
		break ;
		case(12):
			
			
		
		break ;
		case(7):
			con.add(SER_DE.deserr()," " , 0);
			str_text=SER_DE.deserr();
			System.out.println(str_text);
		break ;
		case(8):

			for(Object str : con )
	    	{
	    		
	    		
	    		System.out.println(str);
	    		
	    		
	    		
	    	}
		break ;
		case(9):
			System.out.println(con.size());
		break ;
		case(10):
			System.out.println(con.toString());
		break ;
		case(0):
			System.out.println( ".\n\t\t\t\t\t\t\t\tGoooodbye! \t" );
			System.exit(0);
			break ;
		default:
			break;
		}
		}
	


	}

}
