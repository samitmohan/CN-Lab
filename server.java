import java.io.*;
import java.net.*;

public class server {
    public static void main(String[] args) throws IOException {
        ServerSocket ss = new ServerSocket(4000);
        System.out.println("Server ready for connection");
        Socket s = ss.accept();
        System.out.println("Connection established");

        InputStream inp = s.getInputStream();
        BufferedReader br = new BufferedReader(new InputStreamReader(inp));
        String file_name = br.readLine();
        // file name, content, pw, out
        OutputStream out = s.getOutputStream();
        PrintWriter pw = new PrintWriter(out, true);
        BufferedReader content = new BufferedReader(new FileReader(file_name));
        
        String str;
        while ((str = content.readLine()) != null) pw.println(str);
        s.close(); br.close(); content.close(); pw.close(); ss.close();
    }
}
