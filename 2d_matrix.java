import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		int arr1[][];
		arr1=new int[3][3];
		Scanner input= new Scanner(System.in);
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				int x;
				x=input.nextInt();
				arr1[i][j]=x;
			}
		}
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				System.out.print(arr1[i][j] + " ");
			}
			System.out.println();
		}
	}
}
