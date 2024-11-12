impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        let mut first = std::i32::MAX;
        let mut second = std::i32::MAX;

        for num in nums {
            if num <= first {
                first = num;
            } else if num <= second {
                second = num;
            } else {
                // first < second < num을 만족하므로 True 반환
                return true;
            }
        }
        false
        
    }
}