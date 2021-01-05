package ch.makery.address;

import java.beans.XMLDecoder;
import java.beans.XMLEncoder;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Scanner;

import ch.makery.address.Ser_De_Ser;
import ch.makery.address.model.Domain;


public class File_work<E> {

	
	

	public  StringBuffer path = new  StringBuffer("D:\\Навчання\\Алгоритмізація та програмування\\Прог\\oleh_zherebetskiy\\src\\ua\\lpnuai\\oop\\Zherebetskiy03");

    
   

    
    
 /////////////////////MOVE///////////////////////////////////////////
    public  void MoveForvard(StringBuffer fpath){
       
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

    public  void MoveBack(){
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
    
    public   void WriteF(String filename,String data_s) throws IOException {
		
	    FileOutputStream outputStream = new FileOutputStream(filename.toString()+"\\save.ser");
	    ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);

	    
	    
	    Ser_De_Ser save = new Ser_De_Ser();
	    save.setdata_sInfo(data_s);
	    
	    objectOutputStream.writeObject(save);

	    
	    objectOutputStream.close();
		 }
		 
	public  String ReadF() throws IOException, ClassNotFoundException {

		  FileInputStream fileInputStream = new FileInputStream(path.toString()+"\\save.ser");
		  @SuppressWarnings("resource")
		  ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);

		  Ser_De_Ser saved = (Ser_De_Ser ) objectInputStream.readObject();

		      
		  return saved.toString();
		 }

    


    public void Show() {
        File dir = new File(path.toString());
        if (dir.exists()) {
            File[] inside = dir.listFiles();
            for (File i : inside)
                System.out.println(i);
        }
    }


    public  void WriteXMLE (String filename, ArrayList<E> element) throws IOException{
        try(XMLEncoder encoder = new XMLEncoder(new BufferedOutputStream(new FileOutputStream(filename)))) {
            
           
            encoder.writeObject(element);
            
        }
        catch (FileNotFoundException e){
            System.out.println("file not found");
        }
        
    }
    
    
    
    

    public  ArrayList<Domain> ReadXML(String filename,int i){
        try(XMLDecoder decoder = new XMLDecoder(new BufferedInputStream(new FileInputStream(filename)))){
            @SuppressWarnings("unchecked")
           ArrayList<Domain> object =  (ArrayList<Domain>) decoder.readObject();
       
        		   
           
            if(i==1)
	            	System.out.println(object);
		            return object;
            

        }catch (FileNotFoundException e){
            System.out.println("file not found");
            return new ArrayList<Domain>() ;
        }
    }
	
	

}
