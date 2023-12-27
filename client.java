import java.io.*;
import java.net.*;

public class client {
    public static void main(String[] args) throws IOException {
        Socket s = new Socket("127.0.0.1", 4000);
        System.out.println("Enter file name : ");
        InputStream inp = s.getInputStream();
        OutputStream out = s.getOutputStream();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(out, true);
        String file_name = br.readLine();
        pw.println(file_name);
        BufferedReader content = new BufferedReader(new InputStreamReader(inp));
        String str;
        while ((str = content.readLine()) != null) System.out.println(str);
        s.close(); br.close(); content.close(); pw.close();
    }
}