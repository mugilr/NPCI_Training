import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
			Scanner Sc= new Scanner(System.in);
			System.out.print("enter your first value=");
			int first_value=Sc.nextInt();
			System.out.println(first_value);
			System.out.print("enter your second value=");
			int second_value=Sc.nextInt();
			System.out.println(second_value);
			int square=first_value*first_value;
		if(second_value==square)
		{
		System.out.println(second_value + " is square and multiple of " + first_value); 
		}
		else if(second_value%first_value==0)
		{
		System.out.println(second_value + " is multiple of "+ first_value);
		}
		else
		{
		System.out.println(second_value + " is neither square nor multiple of " +first_value);
		}
	}
}
