#include <cstdio>
#include <queue>
#include <cstring>
#include <time.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
//#include <windows.h>
using namespace std;

#define NODE 100000
#define EDGE 600000
#define MAXK 200
#define SNAP 100

FILE* fp;
FILE* fout;

string node_selection_str;
string threshold;

struct edge
{
    int v, next;
};
edge E[EDGE];

int firstedge[NODE] = {0},
    deg[NODE] = {0},
    degin[NODE] = {0},
    choose[NODE] = {0},
    seed[MAXK] = {0},
    nb[NODE] = {0};
bool visit[NODE] = {0};
int n, m, K,
    TOPK = 20,
    DIR = 0;
float delta[NODE][SNAP] = {0};
float marg[NODE] = {0};

struct myless
{
    bool operator()(int x,int y){
        return marg[x] < marg[y];
    }
};
bool cur[NODE];
priority_queue <int, vector<int>, myless> PQ;

void GenerateThreshold()
{
    for (int i = 0; i < n; i++){
        for (int j = 0; j < SNAP; j++){
            float dt = (float)rand()/RAND_MAX;

            if (string("linear").compare(threshold) == 0) {
              delta[i][j] = dt;
            } else if (string("concave").compare(threshold) == 0) {
              delta[i][j] = dt*dt;
            } else if (string("convex").compare(threshold) == 0) {
              delta[i][j] = sqrt(dt);
            } else if (string("majority").compare(threshold) == 0) {
              delta[i][j] = 0.5;
            }
        }
    }
}

int _Simulate(int snapno,int topk)
{
    queue <int> Q;
    int x,y,i,
        tot = 0;
    float thrs;

    memset(visit,0,sizeof(visit));
    memset(nb,0,sizeof(nb));
    for (i = 0; i < topk; i++){
        Q.push(seed[i]);
        visit[seed[i]] = 1;
        tot++;
    }
    while (!Q.empty()){
        x = Q.front();
        Q.pop();
        for (i = firstedge[x]; i != 0; i = E[i].next){
            y = E[i].v;
            nb[y]++;
            thrs = (float)nb[y]/degin[y];
            if (thrs >= delta[y][snapno] && !visit[y]){
                Q.push(y);
                visit[y] = 1;
                tot++;
            }
        }
    }
    return tot;
}

int Simulate(int snapno,int topk)
{
    if (string("Simulate").compare(node_selection_str) == 0) {
      return _Simulate(snapno, topk);
    } else if (string("Random").compare(node_selection_str) == 0) {
      return (int) rand() % EDGE;
    } else if (string("Degree").compare(node_selection_str) == 0) {
      return deg[seed[topk-1]];
    }

    throw invalid_argument("No supported selection algorithm");
}

int main(int argc, char* argv[])
{
    int x,y,maxj,
        tot=0;
    float maxd,
          totnum=0;
    fp = fopen(argv[1], "r");
    fout = fopen(argv[2], "w");
    srand(time(NULL));

    if (argc >= 4){
        TOPK = atoi(argv[3]);
    }

    if (argc >= 5 && argv[4][0] == 'D'){
        DIR = 1;
    }

    node_selection_str = argv[5];
    threshold = argv[6];

    fscanf(fp, "%d %d", &n, &m);
    for (int i = 0; i < m; i++){
        fscanf(fp, "%d %d", &x, &y);
        tot++;
        E[tot].v = y;
        E[tot].next = firstedge[x];
        firstedge[x] = tot;
        deg[x]++;
        degin[y]++;
        if (DIR == 0){
            tot++;
            E[tot].v = x;
            E[tot].next = firstedge[y];
            firstedge[y] = tot;
            deg[y]++;
            degin[x]++;
        }
    }
    fclose(fp);

    GenerateThreshold(); //for Snapshot

    memset(choose,0,sizeof(choose));

    for (int i = 0; i < n; i++){
        marg[i] = NODE+1;
        PQ.push(i);
    }

    for (int i = 1; i <= TOPK; i++){
        memset(cur,0,sizeof(cur));
        cout << "K: " << i << endl;
        while (1){
            maxj = PQ.top();
            PQ.pop();
            maxd = marg[maxj];
            if (cur[maxj]){
                seed[i-1] = maxj;
                fprintf(fout, "%d %f\n", maxj, maxd);
                break;
            }
            else {
                seed[i-1] = maxj;
                totnum = 0;
                for (int u = 1; u <= SNAP; u++){
                    totnum += Simulate(u, i)-Simulate(u, i-1);
                }
                marg[maxj] = totnum/SNAP;
                cur[maxj] = 1;
                PQ.push(maxj);
            }
        }
    }

    fclose(fout);
    return 0;
}
