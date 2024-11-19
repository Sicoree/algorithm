import java.io.*;
import java.util.*;

public class Main {
    static int cnt, N, M;
    static boolean[] visited;
    static List<Integer>[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        visited = new boolean[N + 1];
        arr = new List[N + 1];
        cnt = 0;
        for(int i = 1; i < N + 1; i++) {
            arr[i] = new ArrayList<Integer>();
        }

        StringTokenizer st;
        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            arr[u].add(v);
            arr[v].add(u);
        }
        BFS(1);

        System.out.println(cnt - 1);
        br.close();
    }

    private static void BFS(int start) {
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(start);

        while(!q.isEmpty()) {
            int x = q.poll();
            if(!visited[x]) {
                cnt++;
                visited[x] = true;
                for(int i = 0; i < arr[x].size(); i++) {
                    q.add(arr[x].get(i));
                }
            }
        }
    }
}
