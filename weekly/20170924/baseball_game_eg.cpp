// baseball game from others
class Solution {
public:
	int calPoints(vector<string>& ops) {
		int i, j, n, ans;
		vector<int> a;
		n = ops.size();
		a.clear();
		for (i=0;i<n;++i) {
			if (ops[i]=="+") {
				a.push_back(a[a.size()-1]+a[a.size()-2]);
			}
			else if(ops[i]=="D") {
				a.push_back(a[a.size()-1]*2);
			}
			else if(ops[i]=="C") {
				a.pop_back();
			}
			else {
				a.push_back(atoi(ops[i].c_str()));
			}
		}
		ans = 0;
		for (i=0;i<a.size();i++)
			ans+=a[i];
		return ans;
	}
};