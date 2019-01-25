'''
55. Given an array of non-negative integers,
you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
'''
// 1. Dynamic Programming Bottom-up: O(n*n)
enum Index{ GOOD, BAD, UNKNOWN }
public class Solution{
  public boolean canJump(int[] nums) {
    Index[] memo = new Index[nums.length];
    for (int i=0; i<memo.length-1; i++){
      memo[i]= Index.UNKNOWN
    }
    memo[memo.length-1] = Index.GOOD

    for (int i=nums.length-2; i>=0; i--){
      int furthestJump = Math.min(i + nums[i], nums.length - 1);
      for (int j=i+1; j<=furthestJump; j++){
        if memo[j]==Index.GOOD{
          memo[i]==Index.GOOD;
          break;
        }
      }
    }
    return memo[0]==Index.GOOD;
  }
}

// 2. Greedy: O(n)
public class Solution{
  public boolean canJumpFromPosition(int[] nums){
    int lasPost = nums.length-1;
    for (int i=nums.length-1; i>=0; i--){
      if (i+nums[i]>=lasPost){ lasPost = i;}
    return lasPost==0;
    }
  }
}


'''
57. Given a set of non-overlapping intervals, insert a new interval into the intervals
(merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
'''
public List<Interval> insert(List<Interval> intervals, Interval newInterval){
  int n = intervals.size();
  int[] starts = new int[n+1];
  int[] ends = new int[n+1];
  List<Interval> res = new ArrayList[]();
  for(int i=0; i<n; i++){
    starts[i] = intervals.get(i).start;
    ends[i] = intervals.get(i).end;
  }
  starts[n]=newInterval.start;
  ends[n]=newInterval.end;

  Arrays.sort(starts);
  Arrays.sort(ends);

  for(int i=0,j=0; i<n+1; i++){
    if(i==n||starts[i+1]>ends[i]){
      res.add(new Interval(starts[j],ends[i]));
      j=i+1;
    }
  }
  return res
}

'''
60. Given n and k, return the kth permutation sequence.
'''
public String getPermutation(int n, int k) {
  int pos=0;
  List<Integer> numbers = new ArrayList<>();
  int [] factorial = new int[n+1];
  StringBuilder sb = new StringBuilder();

  int sum = 1;
  factorial[0] = 1;
  for (int i=1;i<=n;i++){
    sum *= i;
    factotial[i]=sum;
  }

  for(int i=1; i<=n; i++){
    numbers.add(i);
  }
  k--;
  for (int i =1; i<=n; i++){
    int index = k/factorial[n-i];
    sb.append(String.valueOf(numbers.get(index)));
    numbers.remove(index);
    k-=index*factorial[n-i];
  }
  return String.valueOf(sb);
}




'''
data structure
'''
import java.awt.Graphics;
import java.applet.applet;

public class InitArray extends Applet{
  int n[];
  public void init(){
    n = new int[10];
  }

  public void paint(Graphics g){
    int yPst=25;
    g.drawString('Element', 25, yPst);
    g.drawString('Value', 100, yPst);
    for (){}

  }

}
