// 682 baseball game
class Solution {
public:
    int calPoints(vector<string>& ops) {
		score = 0;
	if (ops[0] == "+" or ops[0] == "D" or ops[0] == "C") {
		return;
	}
	if (ops[1] == "+") {
		return;
	}
	int lastValid = ops[0] - "0";
	bool flagLast = true;
	bool flagSecond = false
	for (int i=1; i<ops.size; i++) {
		if (ops[i] >= 0 and ops[i] <= 9) {
			if (flagLast and !flagSecond) {
				flagSecond = true;
				
			}
		}
	}
    }
};