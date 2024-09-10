#include <iostream>
#include <map> // for storage of adjacency list
#include <vector> // for storage of neighbors
#include <queue>
#include <climits> // for int max

using namespace std;

int main() {
    int n,m; // number of rooms and edges

    string s,t;

    cin >> n >> m;

    cin >> s >> t; // s for start t for target
    map <string, vector<string> > g; // this is the graph

    for (int i=0; i<m; i++) {
        string from, to; // iterate through edges
        cin >> from >> to;
        g[from].push_back(to); // this is an undirected graph so has to aadd bothways
        g[to].push_back(from);
    }

    cout << "node B has " << g["B"].size() << endl; // for neighbors

    // implementing BFS
    // need distances
    // parents
    queue<string> bq;

    map<string, vector<string> > parents;
    bq.push(s);

    // point of distance? 
    map<string, int> dist;
    dist[s] = 0;
    parents[s] = "-1";
    for (map<string,vector<string> >::iterator it=g.begin();it!=g.end();it++) {
        dist[it->first] = INT_MAX;
    }

    while (!bq.empty()) {
        string u;
        u = bq.front();
        bq.pop();
        vector<string> neighbors;
        neighbors = g[u];
        for (int i = 0; i<neighbors.size();i++) {
            string v = neighbors[i];
            if (d[u]+1 < d[v]) { // m
            }
        }
    }
}
