package ua.lpnuai.oop.Zherebetskiy02;

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
		System.out.println("Author : Oleh Zherebetskiy \n KN-108 \n "
				+ "Work: In Inputed text change all words which are "
				+ "needed lenght with inputed line \n Comands: \n -a "
				+ "\t data entry \n -b \t data viewing \n -c \t working"
				+ " \n -d \t results \n -ca \t input data to conteiner \n"
				+ " -sf \t save data to file \n -of \t out data from file \n -oc \t out of container \n -os \t out of container \n -cl \t clean container \n -re \t remove first container"
				+ " \n -e \t exit ");
	}
	
	
	
	public static int comscanwork() {
		System.out.print( "..\n.\n.\nCon   sol comand: \t" );
		Scanner scan = new Scanner(System.in);
		
		while(true)
		{	String concon = scan.nextLine();
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
			case("-ca"):
				
				return 5;
			case("-sf"):
	
				return 6;
			case("-of"):
				
				return 7;
			case("-oc"):
				
				return 8;
			case("-os"):
				
				return 10;
			case("-cl"):
				
				return 11;
			case("-re"):
	
				return 12;
			case("-sz"):
				
				return 9;
			default:
				System.out.print( ".\nTry again: \t" );
				break;
			}
		}
	}
}
