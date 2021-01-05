package ua.lpnuai.zherebetskiy04;

import java.io.Serializable;
import java.util.ConcurrentModificationException;
import java.util.Iterator;
import java.util.NoSuchElementException;

import ua.lpnuai.oop.Zherebetskiy02.Container;




@SuppressWarnings("serial")
public class Conteiner<E> implements Iterable<String>, Serializable {
	
	private Array<E> data;
	private Array<E> first;
	@Override
    public Iterator<String> iterator() {
        return new Itr();
    }
	
	public Conteiner ()
	{
		first = new Array<E>();
		
		data=first;
	}
	
private class Itr implements Iterator<String>{
            
	Array<E> data4 =first;
/////////////////////////////////////////////////
        @Override
        public boolean hasNext() {
        	
        	if(data4.next!=null)
            return true;
        	data4=first;
        	return false;
        }
////////////////////////////////////////////////
      
        @Override
        public String next() {

           
            if (!hasNext())
                throw new NoSuchElementException();

            data4=data4.next;
            return data4.toString() ;
            
        }
 //////////////////////////////////////////////////       
        @Override
        public void remove() {
            if (data4.next==null && data4.prev==null)
                throw new IllegalStateException();


            try 
            {
                data4.prev=null;
            } catch (IndexOutOfBoundsException ex) 
            {
                throw new ConcurrentModificationException();
            }
        }
    }
//.....................................................................................................














public void add(E element){
	Array<E> data1 = new Array<E>();
   data1.add(data, element, data.next);
   
}



/////////////////////////////////////////////////
public void out()
{
	
	Array<E> data2 = first;
	StringBuffer s = new StringBuffer();
    do{
    	s.append(data2.data.toString()+"\n\n");
    	data2=data2.next;
        
    }while (data2.next!=null);
    
}
///////////////////////////////////////////////////////  
public boolean contains(E element)

{
	Array<E> data2 = first;
	int index=-1;
    do{
    	if(data2.data.equals(element))
    	{
    		index++;
    		break;
    	}
    	data2=data2.next;
        
    }while (data2.next!=null);
    if (index==-1) 
        return false;
    return true;
}
//////////////////////////////////////////////////////////
public boolean containsAll(Container<E> con1)
{
	
		if(this.equals(con1))
		{
			return false ;
		}
		return true;
	
}

//////////////////////////////////////////////////////////////////////////
public  void clear(){
	data=first.next;
	while(data!=null)		
    data=data.remove();
	data=first;
}
///////////////////////////////////////////////////////////////////////////////
public boolean remove(E text){
    int index=-1;
    data = first.next;
    while(data!=null)
    {
    	if(data.data.equals(text))
    	{
    		index++;
    		data=data.remove();
    	}
    	data=data.next;
    }
        
    
    if (index==-1) 
        return false;
    
    
    return true;
}

//////////////////////////////////////////////////////////////////////////////////
public String toString(){
	
	 
	 StringBuffer stri = new StringBuffer();
	 data = first;
	    while(data!=null)
	    {
	    	stri.append(data.data.toString());
	    }
 	String s = stri.toString();
 	return s;
}

























}
