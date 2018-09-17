import java.io.*;

public class readfile{

  public static void main (String []args) throws Exception{
    String filePath = args[0];
    System.out.println(filePath);

    File file = new File(filePath);
    BufferedReader br = new BufferedReader(new FileReader(file));

    String line;
    while ((line = br.readLine()) != null){
      System.out.println(line);
    }

  }
}
