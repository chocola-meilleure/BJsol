#include<iostream> 
#include<algorithm> // min 함수를 쓰기 위한 헤더 
using namespace std;
#define MAX 55

int N, M; 
char mat[MAX][MAX]; //전체 체스판을 저장할 공간

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) { 
		for (int j = 0; j < M; j++) {  
			cin >> mat[i][j];  
		}
	}
	int ans = 1e9; // 1e9 = 10^9 (도달할 수 없는 큰 값) 
	for (int a = 0; a <= N - 8; a++) {
		for (int b = 0; b <= M - 8; b++) {
			int num1 = 0, num2 = 0; // num1 : 모든 W 홀수 & 모든 B 짝수  num2 : 모든 W 짝수 & 모든 B 홀수 
			for (int i = a; i < a + 8; i++) {
				for (int j = b; j < b + 8; j++) {
					if (mat[i][j] == 'W') {
						if ((i + j) % 2 == 0)num1++; // W를 홀수로 만들어야 하는데 짝수라니깐 반전시키는 비용추가
						else num2++; // W를 짝수로 만들어야 하는데 홀수라니깐 반전시키는 비용추가
					}
					else {
						if ((i + j) % 2 == 0)num2++; // B을 홀수로 만들어야 하는데 짝수라니깐 반전시키는 비용추가
						else num1++; // B을 짝수로 만들어야 하는데 홀수라니깐 반전시키는 비용추가
					}
				}
			}
			ans = min({ ans, num1, num2 });
		}
	}
	cout << ans;
}