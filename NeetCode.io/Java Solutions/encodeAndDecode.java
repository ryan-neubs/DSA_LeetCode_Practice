import java.util.ArrayList;
import java.util.List;

class Solution {

    private int[] lengths;
    private String encoded;

    public String encode(List<String> strs) {
        encoded = "";
        lengths = new int[strs.size()];

        for (int i = 0; i <strs.size(); i++){
            lengths[i] = strs.get(i).length();
            encoded = encoded.concat(strs.get(i));
        }
        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList<String>();

        for (int i = 0; i <lengths.length; i++){
            decoded.add(encoded.substring(0,lengths[i]));
            encoded = encoded.substring(lengths[i]);
        }

        return decoded;
    }
}

