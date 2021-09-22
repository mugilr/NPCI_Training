public class Main {
	public static void main(String[] args) {
	int[] arr1;
	arr1= new int[100];
	arr1[0]=0;
	arr1[1]=1;
	int i;
	for(i=2;i<100;i++)
	{
		if((arr1[i-1]+arr1[i-2])>100)
		{
			break;
		}
		else{
		arr1[i]=arr1[i-1]+arr1[i-2];
	}
	}
	int j;
	for(j=i-1;j>=0;j--)
	{
		System.out.print(" " + arr1[j]);
	}
}
}
