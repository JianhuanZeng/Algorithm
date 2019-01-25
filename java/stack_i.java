//
public static void main(String[] arg){
  StackOfStrings stack = new StackOfStrings();
  while(!StdIn.isEmpty())
  {String s = StdIn.readString();
    if (s.equals('-')) StdOut.print(stack.pop());
    else stack.push(s);}
  }

// linked-list

// N**2

public class LinkedStackOfStrings{
  private Node first = null;

  private class Node{
    String item;
    Node next;
  }

  public boolean isEmpty(){
    return first == null;
  }

  public void push(String item){
    Node oldfirst = first;
    first = new Node();
    first.item = item;
    first.next = oldfirst;}

  public void pop(){
    String item = first.item;
    first = first.next;
    return item;}
}

public class ArrayStackOfStrings{
  private Node first = null;

  private class Node{
    String item;
    Node next;
  }

  public boolean isEmpty(){
    return first == null;
  }

  public void push(String item){
    Node oldfirst = first;
    first = new Node();
    first.item = item;
    first.next = oldfirst;}

  public void pop(){
    String item = first.item;
    first = first.next;
    return item;}
}
