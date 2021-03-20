package ua.lpnuai.oop.Zherebetskiy02;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class SER_DE {

public static void serre(String data_s) throws IOException {
		
	    FileOutputStream outputStream = new FileOutputStream("C:\\Users\\User\\Desktop\\save.ser");
	    ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);

	    
	    
	    Ser_De_Ser save = new Ser_De_Ser();
	    save.setdata_sInfo(data_s);
	    
	    objectOutputStream.writeObject(save);

	    
	    objectOutputStream.close();
		 }
		 
		 public static String deserr() throws IOException, ClassNotFoundException {

		       FileInputStream fileInputStream = new FileInputStream("C:\\Users\\User\\Desktop\\save.ser");
		       @SuppressWarnings("resource")
			ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);

		      Ser_De_Ser saved = (Ser_De_Ser ) objectInputStream.readObject();

		      
		       return saved.toString();
		   }
}
