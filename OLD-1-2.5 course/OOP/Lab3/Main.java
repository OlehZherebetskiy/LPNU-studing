package ua.lpnuai.oop.Zherebetskiy03;


import java.io.IOException;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) throws IOException {
		
		
		
		 System.out.println("Consol comands: \n open - open package \n back - open previous package \n readxml - reading from file \n writexml - writing to the file \n exit - exit ");
		
		Scanner scanner = new Scanner(System.in);
        Work_fl f = new Work_fl();
        String time="";

        while(time!="exit"){
            System.out.print("Your command:");
            time = scanner.nextLine();
            switch (time){
                case "open":
                    Scanner sacn = new Scanner(System.in);
                    System.out.print("File name:");
                    StringBuffer s = new StringBuffer( sacn.nextLine());
                    f.MoveForvard(s);
                    break;
                case "exit":
                    return;
                case "back":
                    f.MoveBack();
                    break;
                case"read":
                    Scanner scn = new Scanner(System.in);
                    System.out.print("Name of file:");
                    String fname1 = scn.nextLine();
                    f.ReadFile(fname1);
                    break;
                case"show":
                    f.Show();
                    break;
                case"writexml":
                    Scanner sc = new Scanner(System.in);
                    System.out.print("Name of file:");
                    String n = sc.nextLine();
                    f.WriteXML(n);
                    break;
                case"readxml":
                    Scanner sc1 = new Scanner(System.in);
                    System.out.print("Name of file:");
                    String n1 = sc1.nextLine();
                    f.ReadXML(n1);
                    break;
            }
        }
        
	}

}
