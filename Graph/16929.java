import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class baekjun_16919 {

    static char[][] board;
    static boolean[][] visited;
    static int n,m;
    static int initx, inity;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    public static boolean dfs(int prevx, int prevy, int startx, int starty) {

        if (visited[startx][starty]) return true;
        visited[startx][starty] = true;

        for(int i = 0; i<4; i++) {
            int newx = startx +dx[i];
            int newy = starty +dy[i];
            if (newx >= 1 && newy >=1 && newx<=n && newy<=m) {
                if ((newx != prevx || newy != prevy) && board[startx][starty] == board[newx][newy]) {
                    if(dfs(startx,starty,newx,newy)) {
                        return true;
                    };
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        board = new char[n+1][m+1];
        visited = new boolean[n+1][m+1];

        for (int i  = 1; i<=n; i++) {
            String s = sc.next();
            for(int j = 1; j<=m ; j++) {
                board[i][j] = s.charAt(j-1);
            }
        }

        for (int i  = 1; i<=n; i++) {
            for(int j = 1; j<=m ; j++) {
                boolean ans = false;
                if (!visited[i][j]) {
                    ans = dfs(0,0,i,j);
                }
                if (ans) {
                    System.out.println("Yes");
                    return;
                }

            }
        }
        System.out.println("No");
    }
}
