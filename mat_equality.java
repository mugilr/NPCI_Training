import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		int arr1[][];
		int arr2[][];
		int eq_matrix[][];
		arr1=new int[2][3];
		arr2= new int[2][3];
		Scanner in =new Scanner(System.in);
		System.out.println("enter 6 element [arr1]");
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<3;j++)
			{
				int x=in.nextInt();
				arr1[i][j]=x;
			}
			System.out.println();
		}
		System.out.println();
    
		System.out.println("enter 6 element [arr2]");
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<3;j++)
			{
				int x=in.nextInt();
				arr2[i][j]=x;
			}
			System.out.println();
		}
		System.out.println();
    
		boolean flag=false;
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<3;j++)
			{
				if(arr1[i][j]==arr2[i][j])
				{
					arr1[i][j]=0;
				}
				else
				{
					flag=true;
				}
			}
		}
		if(flag)
		{
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<3;j++)
			{
				System.out.print(arr1[i][j]+" ");
			}
			System.out.println();
		}
		}
		else{
			System.out.println("Matrix is identical");
		}
	}
} 
