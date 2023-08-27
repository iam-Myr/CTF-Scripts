import java.util.Arrays;

public class EZrev {
    public EZrev() {
    }

    public static void main(String[] var0) {
        	int[] flag = new int[]{130, 37, 70, 115, 64, 106, 143, 34, 54, 134, 96, 98, 125, 98, 138, 104, 25, 3, 66, 78, 24, 69, 91, 80, 87, 67, 95, 8, 25, 22, 115};

            for(int i = 0; i < flag.length / 2; ++i) {
                if (i % 2 == 0) {
                	
                	int var4 = flag[flag.length - 1 - i];
                    flag[flag.length - 1 - i] = (char)(flag[i] - 20);
                    flag[i] = (char)(var4 + 10);
                    
                } else {
                    flag[i] = (char)(flag[i] - 30);
                }
            }
      
            int i;
            for(i = 0; i < flag.length; ++i) {
                 if (i % 2 == 0) { //If even spot
                     flag[i] = (char)(flag[i] ^ 19);
                  } else {
                     flag[i] = (char)(flag[i] ^ 55);
                  }
            }

            print(flag);     
      }
    
    public static void print(int[] array) {
    	for (int i = 0; i< array.length; i++) {
        	System.out.print((char)array[i]);
        }
    	 System.out.println("\n");
        }
    }
