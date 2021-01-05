package ua.lpnuai.oop.surname01;

import java.util.Scanner;

public class Menu {
	
	
	public static boolean prehelp(String arg) {
		if (arg.equals("-h"))
			{
				Menu.help();
				System.exit(0);
				
			}
		 return arg.equals("-d");
	
	}

	
	
	public static void help() {
		System.out.println("Author : Oleh Zherebetskiy \n KN-108 \n Work: In Inputed text change all words which are needed lenght with inputed line \n Comands: \n -a \t data entry \n -b \t data viewing \n -c \t working \n -d \t results \n -e \t exit ");
	}
	
	
	
	public static int comscanwork() {
		System.out.print( ".\n.\n.\nConsol comand: \t" );
		Scanner scan = new Scanner(System.in);
		
		while(true)
		{	String concon = scan.next();
			switch (concon)
			{
			case("-a"):
				return 1;
			
			case("-b"):
				return 2;
	
			case("-c"):
				return 3;
		
			case("-d"):
				return 4;
			
			case("-e"):
				
				return 0;
			default:
				System.out.print( ".\nTry again: \t" );
				break;
			}
		}
	}
}
