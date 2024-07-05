#include <iostream>
#include <string>

#define MAX_N 100000
#define MAX_M 100
#define MAX_P 10000

using namespace std;

// 변수 선언
int n, m, p;
string text, pattern;

// is_pos[i][j] : i번째 까지의 문자열의 접미사와 j번 패턴이 일치하는 경우 true
bool is_pos[MAX_N + 1][MAX_M + 1];

// i번째 패턴의 길이
int pattern_length[MAX_M + 1];

// dp[i] : i번째까지 문자열로 겹치지 않게 선택해 최대로 골라질 수 있는 문자의 수
int dp[MAX_N + 1];

// failure function입니다.
// f[i] : pattern에서 
//        [1, i]로 이루어진 문자열 중
//        접두사와 접미사가 일치하는 최장 길이 (단, 자기자신은 제외)
int f[MAX_P + 1];

int main() {
    // 입력:
    cin >> text >> m;

    n = (int) text.size();

    // 구현의 편의를 위해 맨 앞에 #을 붙여
    // 문자열을 1번지부터 사용합니다.
    text = "#" + text;

    for(int idx = 1; idx <= m; idx++) {
        cin >> pattern;

        p = (int) pattern.size();

        pattern_length[idx] = p;

        // 구현의 편의를 위해 맨 앞에 #을 붙여
        // 문자열을 1번지부터 사용합니다.
        pattern = "#" + pattern;

        // failure function값을 먼저 계산합니다.
        f[0] = -1; // f[0]은 구현의 편의를 위해 -1로 설정합니다.
        for(int i = 1; i <= p; i++) {
            // 시작은 최적의 답에 해당하는 f[i - 1]에서 합니다.
            // 그 전 위치까지 최적의 (접두사, 접미사) 매칭 결과 바로 뒤에
            // 추가되는 것이 가능하다면 최적의 답이 되기 때문입니다.
            int j = f[i - 1];
            // [1, i - 1]까지는
            // 정확히 길이 j만큼 접두사와 접미사가 일치한다고 했을 때
            // 그 다음 문자인 pattern[j + 1]과 pattern[i]가 일치하는지를 확인합니다.
            // 일치하지 않는다면 그 다음 후보로 j값을 옮겨줍니다.
            while(j >= 0 && pattern[j + 1] != pattern[i])
                j = f[j];

            // [1, i - 1]까지 일치하며 동시에 그 다음 문자까지 일치하는 최대 j가 구해져있으므로
            // 이제 그 값에 1을 더한 결과가 f[i]가 됩니다.
            // 매칭에 실패했더라도 f[0]에는 -1이 들어있기에
            // f[i] = 0이 됩니다.
            f[i] = j + 1;
        }
        
        // 한 문자씩 비교하며 패턴 문자열과 일치하게 되는 순간을 구합니다.
        int ans = 0;
        int j = 0;
        for(int i = 1; i <= n; i++) {
            // text의 [i - j, i - 1]와 pattern의 [1, j]가 일치한다는 가정 하여
            // 그 다음 문자인 pattern[j + 1]와 text[i]를 비교합니다.
            // 일치하지 않는다면 f를 이용하여 그 다음 후보로 j값을 빠르게 옮겨줍니다.
            while(j >= 0 && pattern[j + 1] != text[i]) 
                j = f[j];
            
            // 일치하는 곳에서 빠져나온 것이기에
            // 이제 j를 1만큼 증가시킵니다.
            // 매칭에 실패했더라도 j = -1에서 끝났을 것이기에
            // 그 다음 j는 0이 됩니다.
            j++;
            
            // j가 p이 되면 전부 일치했다는 뜻이므로 
            // is_pos 배열을 갱신해주고 다시 그 다음 후보로 넘어갑니다.
            if(j == p) {
                is_pos[i][idx] = true;
                j = f[j];
            }
        }
    }
    
    // is_pos 배열을 바탕으로 dp값을 갱신합니다.
    for(int i = 1; i <= n; i++) {
        dp[i] = dp[i - 1];
        for(int j = 1; j <= m; j++) {
            if(is_pos[i][j]) {
                // 만약 j번째 패턴과 일치하는 경우, j번째 패턴을 이용했을 때의 최댓값은
                // dp[i - pattern_length[j]] + pattern_length[j]입니다.
                // 이 값과 dp[i]를 비교해 최댓값을 갱신해줍니다.
                dp[i] = max(dp[i], pattern_length[j] + dp[i - pattern_length[j]]);
            }
        }
    }
    
    // 문자열 T에서 겹치지 않게 선택해 최대로 골라질 수 있는 문자의 수를 출력합니다.
    cout << dp[n];

    return 0;
}