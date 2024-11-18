use std::collections::HashMap;

impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        
        let mut row_counter: HashMap<Vec<i32>, i32> = HashMap::new();
        for row in &grid {
            *row_counter.entry(row.clone()).or_insert(0) += 1;
        }
        
        let mut col_counter: HashMap<Vec<i32>, i32> = HashMap::new();
        for col in 0..n {
            let mut column = Vec::new();
            for row in 0..n {
                column.push(grid[row][col]);
            }
            *col_counter.entry(column).or_insert(0) += 1;
        }
        
        let mut result = 0;
        for (row, &row_count) in &row_counter {
            if let Some(&col_count) = col_counter.get(row) {
                result += row_count * col_count;
            }
        }

        result
        
    }
}