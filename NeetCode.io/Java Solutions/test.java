


public class test {

     public static void main(String[] args){

        String s = "Was it a car or a cat I saw?";

        s = s.replaceAll("\\p{Space}", "taco");

        System.out.println(s);




     }

    public boolean isPalindrome(String s) {

        s = s.toLowerCase();
        s = s.replaceAll("\\p{Punct}","");


        String newString = new StringBuilder(s).reverse().toString();

        if (newString.equalsIgnoreCase(s)){
            return true;
        }

        return false;
    }
}



