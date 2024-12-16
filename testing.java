public class testing{
    interface func{
        public int test(Integer a, Integer b);
    }
    public static void main(String args[]){
    System.out.println(new func(){
        public int test(Integer a, Integer b){
            return a + b;
        }
    }.test(1, 2));}
}