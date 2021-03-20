package ua.lpnuai.oop.Zherebetskiy02;
import java.io.IOException;
import java.io.Serializable;
import java.util.ConcurrentModificationException;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class Container<E> implements Iterable, Serializable{

    private final int INT_MAS_Siz =16;
    
    public String[] Arra_text = new String[INT_MAS_Siz];
    public String[] Arra_list = new String[INT_MAS_Siz];
	public int[] Arra_lenght = new int[INT_MAS_Siz];
    public int size =0;
    public int point_next;


    @Override
    public Iterator<String> iterator() {
        return new Itr();
    }

    private class Itr implements Iterator<String>{
            
    	
        int last_out = -1; 
        public int point_next=0;
/////////////////////////////////////////////////
        @Override
        public boolean hasNext() {
            return point_next != size;
        }
////////////////////////////////////////////////
      
        @Override
        public String next() {

            int i = point_next;
            if (!hasNext())
                throw new NoSuchElementException();
           String[] array = Container.this.Arra_text;
            if (i >= array.length)
                throw new ConcurrentModificationException();
            point_next = i + 1;
            return Arra_text[last_out = i]+" ///// "+Arra_list[i]+" ////// "+Arra_lenght[i] ;
        }
 //////////////////////////////////////////////////       
        @Override
        public void remove() {
            if (last_out < 0)
                throw new IllegalStateException();


            try 
            {
                Container.this.remove(last_out);
                point_next = last_out;
                last_out = -1;
            } catch (IndexOutOfBoundsException ex) 
            {
                throw new ConcurrentModificationException();
            }
        }
    }
//.....................................................................................................

    
    public void add(int index, String text, String list , int lengh){
        if (index>Arra_text.length){
        	addSize();
        }
        Arra_text[index]=text;
        Arra_list[index]=list;
        Arra_lenght[index]=lengh;
        if (index>size) 
        {
            size=index;
        }
    }
 /////////////////////////////////////////////////////////////
    public int size()
	{
    	return size;
	}
    //////////////////////////////////////////////////
    public void out()
    {
    	
    	Iterator<String> Iter =iterator();
    	for(String str : Arra_text )
    	{
    		
    		if(Iter.hasNext())
    		System.out.println(Iter.next());
    		else break;
    		
    		
    	}
    }
 ///////////////////////////////////////////////////////  
    public boolean contains(String text)

	{
    	int index=-1;
        for (int i =0;i<size;i++){
            if (text.equals(Arra_text[i])){
                index=i;
                break;
            }
        }
        if (index==-1) 
            return false;
        return true;
	}
//////////////////////////////////////////////////////////
    public boolean containsAll(Container<E> con1)
	{
		
			if(Arra_text.equals(con1))
			{
				return false ;
			}
			return true;
		
	}
///////////////////////////////////////////////////////////////
    public void add(String text, String list , int lengh){
        if (size>Arra_text.length){
        	addSize();
        }
        
        Arra_text[size]=text;
        Arra_list[size]=list;
        Arra_lenght[size]=lengh;
        size++;
        
    }
 /////////////////////////////////////////////////////////////////  
    private void addSize(){
    	String[] arra_w =new String[Arra_text.length*2];
        System.arraycopy(Arra_text,0,arra_w,0,size-1);
        Arra_text = arra_w;
        }

//////////////////////////////////////////////////////////////////////////    
    public  void clear(){
        for (int i =0;i<size;i++){
           
            Arra_text[i]=null;
            Arra_list[size]=null;
            Arra_lenght[size]=0;
        }
        size=0;
    }
///////////////////////////////////////////////////////////////////////////////
    public boolean remove(String text){
        int index=-1;
        for (int i =0;i<size;i++){
            if (text.equals(Arra_text[i])){
                index=i;
                break;
            }
        }
        if (index==-1) 
            return false;

        for (int i =index;i<size;i++)
        {
            Arra_text[i]=Arra_text[i+1];
            Arra_list[i]=Arra_list[i+1];
            Arra_lenght[i]=Arra_lenght[i+1];
            
        }
       Arra_text[size-1]=null;
       Arra_list[size-1]=null;
       Arra_lenght[size-1]=0;
       
        size--;
        return true;
    }
///////////////////////////////////////////////////////////////////////////////
    public String remove(int i) {
        if (Arra_text[i] != null) {
            Arra_text[i] = null;
            Arra_list[i] = null;
            Arra_lenght[i] = 0;
            
            System.out.println("Item with index: " + i + " removed!!!");
            size--;
        }
        return Arra_text[i]+"/////"+Arra_list[i]+"//////"+Arra_lenght[i] ;
    }
///////////////////////////////////////////////////////////////////////////////
    public Object[] toArray(){
        return Arra_text;
    }
//////////////////////////////////////////////////////////////////////////////////
    public String toString(){
    	
    	 Iterator<String> Iter =iterator();
    	 StringBuffer stri = new StringBuffer();
     	for(String str : Arra_text )
     	{
     		
     		if(Iter.hasNext())
     		stri.append(Iter.next());
     		else break;
     		
     		
     	}
     	String s = stri.toString();
     	return s;
    }

}



