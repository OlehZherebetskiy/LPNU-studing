package ua.lpnuai.oop.Zherebetskiy02;
import java.io.Serializable;

public class Ser_De_Ser implements Serializable {

	private static final long serialVersionUID = 1L;
	private String data_s;
	
	public String getdata_sInfo() {
	       return data_s;
	   }

	   public void setdata_sInfo(String data_s) {
	       this.data_s = data_s;
	   }
	
	@Override
	   public String toString() {
	       return data_s;
	}
}
