#include <iostream>
#include <string>

#define MAX_M 100000

using namespace std;

// 변수 선언
int n, m;
string text, pattern;

// failure function입니다.
// f[i] : pattern에서 
//        [1, i]로 이루어진 문자열 중
//        접두사와 접미사가 일치하는 최장 길이 (단, 자기자신은 제외)
int f[MAX_M + 1];

int main() {
    // 입력:
    cin >> text;

    n = (int) text.size();

    // 구현의 편의를 위해 맨 앞에 #을 붙여
    // 문자열을 1번지부터 사용합니다.
    text = "#" + text;

    // 답을 1 ~ n 사이의 값으로 결정한 뒤
    // 구간을 탐색하는 이분 탐색을 진행합니다.
    int lo = 1;
    int hi = n;
    int ans = 1;

    while(lo <= hi) {
        int mid = (lo + hi) / 2;

        // 앞 mid개의 접두사를 뒤집은 값이 pattern입니다.
        pattern = "";
        for(int i = mid; i >= 1; i--)
            pattern += text[i];
        
        m = (int) pattern.size();
        
        // 구현의 편의를 위해 맨 앞에 #을 붙여
        // 문자열을 1번지부터 사용합니다.
        pattern = "#" + pattern;

        // failure function값을 먼저 계산합니다.
        f[0] = -1; // f[0]은 구현의 편의를 위해 -1로 설정합니다.
        for(int i = 1; i <= m; i++) {
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
        bool is_substring = false;
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
            
            // j가 m이 되면 전부 일치했다는 뜻이므로 
            // 답을 갱신해줍니다.
            if(j == m) {
                is_substring = true;
                break;
            }
        }

        // 앞 mid개의 접두사를 뒤집은 것이
        // substring이라면, 정답을 갱신해주고
        // 그보다 큰 구간에서 탐색합니다.
        if(is_substring) {
            ans = mid;
            lo = mid + 1;
        }
        // 반대의 경우 그보다 작은 구간에서 탐색합니다.
        else {
            hi = mid - 1;
        }
    }
    
    // 부분 문자열인 가장 긴 뒤집힌 접두사의 길이를 출력합니다.
    cout << ans;

    return 0;
}