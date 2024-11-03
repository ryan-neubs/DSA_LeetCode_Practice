import java.util.HashMap;

/*

Given an array of integers nums and an integer target,
 return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of
 indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:

Input:
nums = [3,4,5,6], target = 7
Output: [0,1]


Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000

 */


public class twoSum {


    public int[] twoSum(int[] nums, int target) {

        //Create a new hashmap
        HashMap<Integer, Integer> prevMap = new HashMap<>();

        //Loop through the length of given array
        for (int i = 0; i < nums.length; i++) {
            //Declare and initialize @int num with value given at index i of @array nums
            int num = nums[i];
            //Declare and initialize @int diff with the given @int target - @int num (current value at index)
            int diff = target - num;


            //if the hashmap contains the value given by
            //the difference of the target value - current value at index
            //
            //return a new array of type @int with the value of @HashMap prevMap with the given
            //key @int diff
            if (prevMap.containsKey(diff)) {
                return new int[] { prevMap.get(diff), i };
            }

            //associate the value @int i with the key @int diff
            prevMap.put(num, i);
        }

        //return empty int[]
        return new int[] {};
    }
}

