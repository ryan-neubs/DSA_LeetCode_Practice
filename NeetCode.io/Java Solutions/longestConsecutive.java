import java.util.HashSet;

    public class longestConsecutive {

        public int longestConsecutive(int[] nums) {
            HashSet<Integer> cons = new HashSet<>();
            int longest = 0;
            int currentLongest = 0;

            for(int i = 0; i <nums.length; i++){
                cons.add(nums[i]);
            }

            if (!cons.isEmpty()){
                currentLongest=1;
            }else {
                return 0;
            }


            //[0,1,2,6,5,3,8,10,14]
            for(int i = 0 ; i < nums.length; i++) {

                if (!cons.contains(nums[i] - 1)) { //if set does not contain a number less than the number at current index
                    while (cons.contains(nums[i] + currentLongest)) { //while the set contains a number greater than the number at current index + currentlongest
                        currentLongest++;    //increment longest sequence
                    }
                }
                if (currentLongest > longest){
                    longest = currentLongest;
                }
                currentLongest =1;
            }

            return longest;
        }
    }

