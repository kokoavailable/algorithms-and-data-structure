use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut freq = HashMap::new();
        
        for &num in &arr {
            *freq.entry(num).or_insert(0) += 1;
        }
        
        let occurrences: HashSet<_> = freq.values().collect();
        freq.len() == occurrences.len()
    }
}