impl Solution {
    pub fn longest_ones(nums: Vec<i32>, k: i32) -> i32 {
        let(mut i, mut zero_cnt, mut max_len) = (0, 0, 0);
            for j in 0..nums.len() {
                if nums[j] == 0{
                    zero_cnt += 1;
                }
            
                while zero_cnt > k {
                   if nums[i as usize] == 0 {
                       zero_cnt -= 1;
                    }
                    i += 1;
                }
                max_len = max_len.max((j as i32) - i + 1);
                
            }
            max_len
//         let (mut i, mut max_len, mut zero_cnt) = (0, 0, 0);
//         for j in 0..nums.len() {
//             if nums[j] == 0 {
//                 zero_cnt += 1;
//             }
        
//             while zero_cnt > k {
//                 if nums[i as usize] == 0 {
//                     zero_cnt -= 1;
//                 }
//                 i += 1;
//             }
//             max_len = max_len.max((j as i32) - i + 1);
//         }
//         max_len
    }
}