package ch.makery.address;

import java.util.Scanner;

public class Menu {

	static int  k=99;

	public static boolean prehelp(String arg) {
		if (arg.equals("-h"))
			{
				Menu.help();
				System.exit(0);
				
			}
		 return arg.equals("-auto");
	
	}

	
	
	public static void help() {
		System.out.println("Author : Oleh Zherebetskiy \n KN-108 \n "
				+ "Work: In Inputed text change all words which are "
				+ "needed lenght with inputed line \n Comands: \n -in "
				+ "\t buffer input \n -add \t add from buffer to conteiner \n -out \t output conteiner\'s data\n -sort \t sort conteiner data "
				+ " \n -ifco \t find data \n -remove \t delete element \n"
				+ " -clear \t clean the conteiner \n -writexml \t write at txt file \n -readxml \t read from txt file to conteiner\n -write \t write to serialized file \n -read \t read from serialized file to buffer \n -open \t open directory"
				+  "\n -back \t go to previous package \n -show \t show all files in package \n -e \t exit ");
	}
	
	
	
	public static int comscanwork(boolean p) {
		if(!p)
		System.out.print( "..\n.\n.\nCon   sol comand: \t" );
		Scanner scan = new Scanner(System.in);
		
		while(true)
			
		{	String concon;
			
			if(p) {k++; System.out.println( "..\n.\n.\nCon   sol comand: \t "+ k );return k ;
			}
			
			concon = scan.nextLine();
			switch (concon )
			{
			case "-in" : //in
				return 11;
			
			case "-fastin" : //in
				return 16;
			case "-intimelimit" : 
				return 18;
			case "-snames" : 
				return 19;
			case "-rands" : 
				return 22;
				
			case "-parsearch" : 
				return 20;
			case "-possearch" : 
				return 21;
			
			case("-add"): //add
				return 1;
			
			case("-out")://out
				return 2;
	
			case("-ifco")://if contains
				return 3;
			case("-e"): 
				return 0;
			case("-remove"):
				return 4;
			
			case("-clear"):
				
				return 5;
			case("-writexml"): case("3"):
				
				return 6;
			case("-readxml"): case("4"):
	
				return 7;
			case("-write"):
				
				return 8;
			case("-read"):
				
				return 9;
			case("-sort"):
				
				return 15;
			case("-open"):
				
				return 10;
			case("-back"):
	
				return 12;
			case("-show"):
	
				return 13;
			default:
				System.out.print( ".\nTry agai n: \t" );
				break;
			}
		}
	}
}
