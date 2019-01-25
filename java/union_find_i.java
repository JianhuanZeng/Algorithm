public class QuickFindUF{
  private int[] id;

  public QuickFindUF(int N){
    id = new int[N];
    for (int i=0; i<N; i++){
      id[i]=i;
    }
  }

  public boolean connected(int q, int p){
    return id[q]==id[p];
  }

  public void union(int q, int p){
    int pid = id[p];
    int qid = id[q];
    for (int i=0; i<N; i++){
      if(id[i]== pid) id[i]=qid;
    }
  }
}
// N**2

public class QuickUnionUF{
  private int[] id;

  public QuickFindUF(int N){
    id = new int[N];
    for (int i=0; i<N; i++) id[i]=i;
    sz = new int[N];
    for (int i=0; i<N; i++) id[i]=1;
  }

  private int root(int i){
    while (i!=id[i]){ id[i]=id[id[i]]; i = id[i];}
    return i;
  }

  public boolean connected(int q, int p){
    return root(q) == root(p);
  }

  public void union(int q, int p){
    int i = root(q);
    int j = root(p);
    if (i == j) return;
    if (sz[i]<sz[j]) {id[i] = j;sz[j]+=sz[i];}
    else             {id[j] = i;sz[i]+=sz[j];}

}
// N -> lg N
