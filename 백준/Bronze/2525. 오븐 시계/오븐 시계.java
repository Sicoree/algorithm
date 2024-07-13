import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String s = br.readLine();
		StringTokenizer st = new StringTokenizer(s, " ");

		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(br.readLine());
		int D = B + C;

		int m = 60 * A + B;
		m += C;
		
		int hour = (m / 60) % 24;
		int minute = m % 60;
		
		System.out.println(hour + " " + minute);
	}
}
