
class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("\\p{Punct}","");
        s = s.replaceAll("\\p{Space}", "");
        String newString = new StringBuilder(s).reverse().toString();
        if (newString.equalsIgnoreCase(s)){
            return true;
        }
        return false;
    }
}

