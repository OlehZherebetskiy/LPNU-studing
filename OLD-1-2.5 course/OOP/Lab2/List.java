package ua.lpnuai.oop.Zherebetskiy02;

import java.util.Scanner;

public class List {

	public static String scan_text() {
		System.out.print( ".\nInput text: \t" );
		Scanner scan = new Scanner(System.in);
		return scan.nextLine();
	}
	public static String scan_list() {
		System.out.print( ".\nInput line: \t" );
		Scanner scan = new Scanner(System.in);
		return scan.nextLine();
	}
	public static int scan_word() {
		System.out.print( ".\nWord lenght: \t" );
		Scanner scan = new Scanner(System.in);
		int k;
		do {
			k= scan.nextInt();
			if (k  <= 0 ) System.out.print( "\nTry again: \t" );
		}
		while(k<=0);
		return k;
	}
	
	public static void Out_d(String s1,String s2,int s3) {
		System.out.println("Text:\t"+s1+"\nList:\t"+s2+"\nWord lenght:\t"+s3+"\n");
		
	}

	public static String str_work(String s1,String s2,int s3,boolean deb) {
		String str_text = new String();
		
		s1+=" \0";
		if (deb==true) System.out.println("Add to text end sign (+\" \\0\")");
		char wor[]=s1.toCharArray();
	    int i=0,numl= 0 , point=0;
	    if (deb==true) System.out.println( "\nVeriable for moveing srought ( i = 0 ), word length (numl = 0), calculation mod point = 0\n");
		do
	    {   
			if (point == 0 )
			{
				if(wor[i]!=' ')
		    	{
		    		
		    		point=1;
		    		numl++;
		    		if (deb==true) System.out.println("\npoint: "+point+"\tnuml: "+numl);
		    	}
				else 
				{
					str_text += wor[i]; if (deb==true) System.out.println("\nText:\t "+str_text);
				}
			}
			else
			{
				if(wor[i]==' ')
		    	{
		    		
		    		point=0;if (deb==true) System.out.println("\npoint: "+point+"\tEnd of word)");
		    		if (numl==s3)
		    		{
		    			
		    			str_text += s2;
		    			str_text += wor[i];
		    			if (deb==true) System.out.println("\nText:\t"+str_text);
		    		}
		    		else
		    		{
		    			for(int j=numl;j>=0; j--)
		    			{
		    				str_text += wor[i-j];if (deb==true)System.out.println("\nText:\t"+str_text);
		    			}
		    		}
		    		numl=0; if (deb==true)System.out.println("\nnuml:\t"+numl+"\tEnd of word");
		    		
		    	}
				else
				{
					numl++;if (deb==true)System.out.println("\nnuml:\t"+numl+"\tWord lenght calculating");
					
				}
			}
			
			i++; if (deb==true)System.out.println("\ni:\t"+i+"\t-char number");
	    }
		while (wor[i]!='\0');
		System.out.println( ".\nWork done! \t" );
		return str_text;
	}
	
}
