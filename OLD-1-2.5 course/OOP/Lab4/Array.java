package ua.lpnuai.zherebetskiy04;



public class Array<E> {

		E  data;
		Array<E> next;
		Array<E> prev;
		
		
		
		public void add (Array<E> prev , E element , Array<E> next)
		{
			
			this.data = element;
			this.next= next;
			this.prev= prev;
			if(this.next!=null)
			next.prev= this;
			prev.next= this;
			
			
		}
		public void add (Array<E> prev , E element )
		{
			
			this.data = element;
			this.next= prev.next;
			this.prev= prev;
			if(this.next!=null)
			prev.next.prev= this;
			prev.next= this;
			
		}
		
		public Array<E> remove()
		{
			if( next!=null)
			{
				
				next.prev=prev;
			}
			prev.next=next;
			
			return next;
			
		}
		
		
		@Override
		public String toString()
		{
			return data.toString();
		}
}

