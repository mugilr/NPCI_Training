import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		int arr1[][];
		int arr2[][];
		arr1=new int[2][3];
		arr2= new int[2][3];
		Scanner in =new Scanner(System.in);
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<3;j++)
			{

				int x=in.nextInt();
				arr1[i][j]=x;
				System.out.print(x+" ");
			}
			System.out.println();
		}
		System.out.println();
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<3;j++)
			{

				int x=in.nextInt();
				arr2[i][j]=x;
				System.out.print(x+" ");
			}
			System.out.println();
		}
		System.out.println("sum of matrix arr1 and arr2");
		System.out.println();
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<3;j++)
			{
				int x=arr1[i][j]+arr2[i][j];
				System.out.print(x+" ");
			}
			System.out.println();
		}
	}
}
