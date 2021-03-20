package ua.lpnuai.oop.surname01;

public class Main {

	public static void main(String[] args) {
		boolean Point = false;
		
		if (args.length > 0)  Point = Menu.prehelp(args[0]) ;
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
			str_text = List.str_work(str_text, str_list, word,Point);
		if (Point==true) List.Out_d(str_text, str_list, word);
			break ;
		case(4):
			System.out.println("\nText:\t"+str_text);
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
