import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        try {
            int n = Integer.parseInt(reader.readLine()); // 계단의 개수

            int[] scores = new int[n + 1]; // 각 계단의 점수를 저장할 배열
            int[] dp = new int[n + 1]; // 각 계단까지의 최대 점수를 저장할 배열

            for (int i = 1; i <= n; i++) {
                scores[i] = Integer.parseInt(reader.readLine());
            }

            dp[1] = scores[1]; // 첫 번째 계단은 그대로 점수를 사용
            if (n >= 2) {
                dp[2] = scores[1] + scores[2]; // 두 번째 계단까지의 최대 점수는 첫 번째와 두 번째 계단의 점수를 합친 값
            }

            for (int i = 3; i <= n; i++) {
                dp[i] = Math.max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i]);
                // i번째 계단까지의 최대 점수는 (i-2번째 계단까지의 최대 점수 + i번째 계단의 점수)와 (i-3번째 계단까지의 최대 점수 + i-1번째 계단의 점수 + i번째 계단의 점수) 중 더 큰 값
            }

            System.out.println(dp[n]); // 마지막 계단까지의 최대 점수 출력

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
