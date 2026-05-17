#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    unordered_map<string, int> rank_map;
    for (int i = 0; i < players.size(); i++) {
        rank_map[players[i]] = i;
    }

    for (const string& name : callings) {
        int idx = rank_map[name];

        rank_map[players[idx - 1]] = idx;     // 앞 사람 순위 +1
        rank_map[name] = idx - 1;             // 호명된 사람 순위 -1
        swap(players[idx], players[idx - 1]); // 배열도 교체
    }

    return players;
}