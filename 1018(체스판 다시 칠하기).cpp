#include<iostream> 
#include<algorithm> // min �Լ��� ���� ���� ��� 
using namespace std;
#define MAX 55

int N, M; 
char mat[MAX][MAX]; //��ü ü������ ������ ����

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) { 
		for (int j = 0; j < M; j++) {  
			cin >> mat[i][j];  
		}
	}
	int ans = 1e9; // 1e9 = 10^9 (������ �� ���� ū ��) 
	for (int a = 0; a <= N - 8; a++) {
		for (int b = 0; b <= M - 8; b++) {
			int num1 = 0, num2 = 0; // num1 : ��� W Ȧ�� & ��� B ¦��  num2 : ��� W ¦�� & ��� B Ȧ�� 
			for (int i = a; i < a + 8; i++) {
				for (int j = b; j < b + 8; j++) {
					if (mat[i][j] == 'W') {
						if ((i + j) % 2 == 0)num1++; // W�� Ȧ���� ������ �ϴµ� ¦����ϱ� ������Ű�� ����߰�
						else num2++; // W�� ¦���� ������ �ϴµ� Ȧ����ϱ� ������Ű�� ����߰�
					}
					else {
						if ((i + j) % 2 == 0)num2++; // B�� Ȧ���� ������ �ϴµ� ¦����ϱ� ������Ű�� ����߰�
						else num1++; // B�� ¦���� ������ �ϴµ� Ȧ����ϱ� ������Ű�� ����߰�
					}
				}
			}
			ans = min({ ans, num1, num2 });
		}
	}
	cout << ans;
}