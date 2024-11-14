impl Solution {
    pub fn max_operations(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort();
        
        let mut cnt = 0;
        let (mut i, mut j) = (0, nums.len() - 1);
        
        while i < j {
            let sum = nums[i] + nums[j];
            if sum == k {
                cnt += 1;
                i += 1;
                j -= 1;
            } else if sum < k {
                i += 1;
            } else {
                j -= 1;
            }
        }
        
        cnt
    }
}