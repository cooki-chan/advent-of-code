import java.util.*;
import java.io.*;
public class Day21{
   public static void main(String[] args) throws Exception{
      System.out.println("Part 1 or 2?");
      if(new Scanner(System.in).next().equals("1")){
         System.out.println("Solving for Part 1");
         System.out.println(part1());
      }
      else{
         System.out.println("Solving for Part 2");
         System.out.println(part2());
      }
   }
   public static int part1() throws Exception{
      int count = 0;
      Scanner scanner = new Scanner(new File("Day21.txt"));
      while(scanner.hasNextLine()){
         String temp = scanner.nextLine();
         int x = 2, y = 3;
         int moves = 0;
         for(int i = 0; i < temp.length(); i++){
            moves+=getCode(x, y, getX(temp.charAt(i)), getY(temp.charAt(i)), 3, 0);
            x = getX(temp.charAt(i));
            y = getY(temp.charAt(i));
         }
         System.out.println(""+moves);
         count+=moves*Integer.parseInt(temp.substring(0,3));
      }
      return count;
   }
   public static long part2() throws Exception{
      long count = 0;
      Scanner scanner = new Scanner(new File("Day21.txt"));
      while(scanner.hasNextLine()){
         String temp = scanner.nextLine();
         int x = 2, y = 3;
         long moves = 0;
         String temp2 = "";
         for(int i = 0; i < temp.length(); i++){
            long temp3 = getCode(x, y, getX(temp.charAt(i)), getY(temp.charAt(i)), 26, 0);
            x = getX(temp.charAt(i));
            y = getY(temp.charAt(i));
            moves+=temp3;
         }
         System.out.println(moves);
         count+=moves*Integer.parseInt(temp.substring(0,3));
      }
      return count;
   }
   private static char[][] dirs = {{' ', '^', '*'},{'<','v','>'}};
   private static char convertToDir(int x, int y){
      return dirs[y][x];
   }
   private static char[][] nums = {{'7', '8', '9'},{'4','5','6'},{'1','2','3'},{' ','0','A'}};
   private static char convertToNum(int x, int y){
      return nums[y][x];
   }
   private interface Converter{
      abstract String convert(int pos1, int pos2);
   }
   static HashMap<String, Long> cache = new HashMap();
   static Converter[] dirsFunc = {
      (x,gX) -> {if(gX < x){String temp = ""; for(int i = 0; i < x-gX; i++){temp+="<";} return temp;}else{String temp = ""; for(int i = 0; i < gX-x; i++){temp+=">";} return temp;}},
      (x,gX) -> {if(gX < x){String temp = ""; for(int i = 0; i < x-gX; i++){temp+="^";} return temp;}else{String temp = ""; for(int i = 0; i < gX-x; i++){temp+="v";} return temp;}}};
   private static long getCode(int x, int y, int gX, int gY, int up, int gen){
      if(gen > 0 && cache.containsKey(gen+""+convertToDir(x, y)+""+convertToDir(gX, gY))){
         return cache.get(gen+""+convertToDir(x, y)+""+convertToDir(gX, gY));
      }
      long temp = 0;
      if(gY == y){
         temp = getCode(dirsFunc[0].convert(x,gX)+"*", up-1, gen+1);
         if(gen > 0){
            cache.put(gen+""+convertToDir(x, y)+""+convertToDir(gX, gY),temp);
         }
         return temp;
      }
      else if(gX == x){
         temp = getCode(dirsFunc[1].convert(y,gY)+"*", up-1, gen+1);
         if(gen > 0){
            cache.put(gen+""+convertToDir(x, y)+""+convertToDir(gX, gY),temp);
         }
         return temp;
      }
      else{
         if(gen == 0 && x == 0 && gY == 3){
            return getCode(dirsFunc[0].convert(x,gX)+dirsFunc[1].convert(y,gY)+"*", up-1, gen+1);
         }
         if(gen == 0 && y == 3 && gX == 0){
            return getCode(dirsFunc[1].convert(y,gY)+dirsFunc[0].convert(x,gX)+"*", up-1, gen+1);
         }
         if(gen > 0 && y == 0 && gX == 0){
            temp = getCode(dirsFunc[1].convert(y,gY)+dirsFunc[0].convert(x,gX)+"*", up-1, gen+1);
            cache.put(gen+""+convertToDir(x, y)+""+convertToDir(gX, gY),temp);
            return temp;
         }
         if(gen > 0 && x == 0 && gY == 0){
            temp = getCode(dirsFunc[0].convert(x,gX)+dirsFunc[1].convert(y,gY)+"*", up-1, gen+1);
            cache.put(gen+""+convertToDir(x, y)+""+convertToDir(gX, gY),temp);
            return temp;
         }
         temp = getCode(dirsFunc[0].convert(x,gX)+dirsFunc[1].convert(y,gY)+"*", up-1, gen+1);
         long temp1 = getCode(dirsFunc[1].convert(y,gY)+dirsFunc[0].convert(x,gX)+"*", up-1, gen+1);
         if(temp1 < temp){
            temp = temp1;
         }
         if(gen > 0){
            cache.put(gen+""+convertToDir(x, y)+""+convertToDir(gX, gY),temp);
         }
      }
      return temp;
   }
   private static long getCode(String code, int up, int gen){
      if(up == 0){
         return code.length();}
      long temp = 0;
      int x = 2, y = 0;
      for(int i = 0; i < code.length(); i++){
         int gX = getX(code.charAt(i)), gY = getY(code.charAt(i));
         temp += getCode(x,y, gX, gY, up, gen);
         x = gX;
         y = gY;
      }
      return temp;
   }
   private static int getX(char c){
      if(c == '7' || c == '4' || c == '1' || c == '<'){
         return 0;
      }
      if(c == '8' || c == '5' || c == '2' || c == '0' || c == '^' || c == 'v'){
         return 1;
      }
      return 2;
   }
   private static int getY(char c){
      if(c == '7' || c == '8' || c == '9' || c == '^' || c == '*'){
         return 0;
      }
      if(c == '4' || c == '5' || c == '6' || c == '<' || c == '>' || c == 'v'){
         return 1;
      }
      if(c == '1' || c == '2' || c == '3'){
         return 2;
      }
      return 3;
   }
}