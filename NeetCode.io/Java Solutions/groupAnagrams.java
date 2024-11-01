import java.util.*;


    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> res = new HashMap<>();


        //For each string s in strs String[]
        for (String s : strs) {

            //create a new int[] count
            int[] count = new int[26];

            //for each character c in char[] s
            for (char c : s.toCharArray()) {

                //count at index[c-'a'] increments
                /*
                c - 'a': This calculates the position of the character c relative to 'a'. For example:
                If c is 'a', then c - 'a' is 0.
                If c is 'b', then c - 'a' is 1.
                If c is 'z', then c - 'a' is 25.
                This effectively maps each character 'a' to 'z' to a specific index in the count array, ranging from 0 to 25.
                */
                count[c - 'a']++;
            }

            //Arrays.toString(count): This converts the count array to a string representation.
            //
            //For instance, if count represents the string "abb" (with count = [1, 2, 0, 0, ..., 0]),
            //then Arrays.toString(count) will produce a string like "[1, 2, 0, 0, ..., 0]".
            //This stringified version of count captures the frequency of each letter in a fixed order (from 'a' to 'z').
            //As a result, different strings that are anagrams (like "bba" and "abb") will produce the same key since their character frequencies match.
            String key = Arrays.toString(count);

            //if the key isnt present, put in the new key i.e "[1, 2, 0, 0, ..., 0]" with the value new empty Arraylist
            res.putIfAbsent(key, new ArrayList<>());
            //retrieves list associated with the key, i.e "[1, 2, 0, 0, ..., 0]"
            //then adds the current string s to the specified list
            res.get(key).add(s);
        }
        //return a new list using only the values (lists of anagrams) of res
        return new ArrayList<>(res.values());
    }
}