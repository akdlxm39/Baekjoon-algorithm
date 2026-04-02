#include <iostream>
#include <vector>

using namespace std;

int n;
int nums[101];
bool isCycle[101];
bool visited[101];
bool checked[101];
int ans;
vector<int> st;

int checkCycle(int cur)
{
    if (visited[cur])
        return cur;
    if (checked[cur])
        return 0;
    checked[cur] = true;
    visited[cur] = true;
    st.push_back(cur);
    int root = checkCycle(nums[cur]);
    visited[cur] = false;
    if (root == cur)
    {
        while (true)
        {
            int tmp = st.back();
            st.pop_back();
            isCycle[tmp] = true;
            ans++;
            if (cur == tmp)
                break;
        }
        return 0;
    }
    return root;
}

void solve()
{
    cin >> n;
    for (int i = 1; i <= n; ++i)
        cin >> nums[i];
    for (int i = 1; i <= n; ++i)
    {
        if (!checked[i])
        {
            st.clear();
            checkCycle(i);
        }
    }
    cout << ans << '\n';
    for (int i = 1; i <= n; ++i)
        if (isCycle[i])
            cout << i << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}