import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	int first_value= in.nextInt();
	int real_value=first_value;
	int count1=0;
	while(first_value > 0)
	{
	  first_value=first_value/10;
	  count1++;
	}
	if(count1==1)
	System.out.println(real_value);
	else if(count1==3)
	{
	System.out.println(count1*count1*count1);
	}
	else if(count1%2==0)
	{
	System.out.println(count1*count1);
	}
	else if(count1%2==1)
	{
	count1--;
	  System.out.println(count1*count1);
	}
}
}
