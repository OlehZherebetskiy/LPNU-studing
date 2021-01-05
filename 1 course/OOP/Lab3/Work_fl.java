package ua.lpnuai.oop.Zherebetskiy03;


import java.beans.XMLDecoder;
import java.beans.XMLEncoder;
import java.io.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;


public class Work_fl {
	
	
	public StringBuffer path = new  StringBuffer("D:\\Навчання\\Алгоритмізація та програмування\\Прог\\oleh_zherebetskiy\\src\\ua\\lpnuai\\oop\\Zherebetskiy03");

    
    protected ArrayList<Catalog> goods = new ArrayList<Catalog>();

    
    
 /////////////////////MOVE///////////////////////////////////////////
    public void MoveForvard(StringBuffer fpath){
       
    	path.append("\\"+fpath);
        File dir = new File(path.toString());
        File[] inside = dir.listFiles();
        if (dir.exists()) {
            for (File i : inside)
                System.out.println(i);
        }
        else
            System.out.println("no such directory");
    }

    public void MoveBack(){
        File dir = new File(path.toString());
        StringBuffer parent = new StringBuffer( dir.getParent());
        path = parent;
        File pardir = new File(path.toString());
        if(pardir.exists()) {
            File[] inside = pardir.listFiles();
            for (File i : inside)
                System.out.println(i);
        }else{
            System.out.println("you're in the root");
        }
    }
/////////////////////////////////////////////////////////////////////////////////
    

    
    public void ReadFile(String fileName){
        try(FileReader reader = new FileReader(fileName))
        {
            Scanner read = new Scanner(reader);
            while(read.hasNextLine()){
                System.out.println(read.nextLine());
            }
            
            read.close();
        }
        catch (IOException e){
            System.out.println("can not read a file");
        }
        
    }

    public void Show() {
        File dir = new File(path.toString());
        if (dir.exists()) {
            File[] inside = dir.listFiles();
            for (File i : inside)
                System.out.println(i);
        }
    }


    public void WriteXML(String filename) throws IOException{
        try(XMLEncoder encoder = new XMLEncoder(new BufferedOutputStream(new FileOutputStream(filename)))) {
            Scanner sc = new Scanner(System.in);
            String m = "add"; 
            
            while (!m.equals("done")) {
               
                switch (m) {
                    case "add":
                        
                    goods.add(new Catalog(1));
                     
                       break;
                       
                }
                System.out.println("add more info about -'add', else 'done'");
                
                m = sc.nextLine();
            }
            encoder.writeObject(goods);
            
        }
        catch (FileNotFoundException e){
            System.out.println("file not found");
        }
    }
    
    
    
    

    public void ReadXML(String filename){
        try(XMLDecoder decoder = new XMLDecoder(new BufferedInputStream(new FileInputStream(filename)))){
            @SuppressWarnings("unchecked")
			ArrayList<Catalog> object =  (ArrayList<Catalog>) decoder.readObject();
           
            for(Catalog g : object)
            {
	            System.out.print(g.getName() + g.getUnit() + g.getUnit_price()+g.getNumber() + g.getReceipt_d());
	           ArrayList<String> str =new ArrayList<String>(g.getAbout());
	            for(String s : str )
		            {
	            	System.out.println(s);
		            }
            }

        }catch (FileNotFoundException e){
            System.out.println("file not found");
        }
    }
	
	

}
