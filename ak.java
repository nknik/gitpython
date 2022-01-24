
import java.io.*;
  
interface In1
{
    final int a = 10;
  
    void display();
}
  
class TestClass implements In1
{
    public void display()
    {
        System.out.println("1");
    }
  
    public static void main(String[] args)
        throws IOException
    {
 
        BufferedReader bi = new BufferedReader(
            new InputStreamReader(System.in));
 
        int num[] = new int[10];
        String[] strNums;
 
 
        strNums = bi.readLine().split(" ");
 
        for (int i = 0; i < strNums.length; i++) {
            num[i] = Integer.parseInt(strNums[i]);
        }
        TestClass t = new TestClass();
        t.display();
    }

}