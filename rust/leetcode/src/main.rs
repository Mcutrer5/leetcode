mod minimum_distance;
use minimum_distance::Solution;
fn main() {
   minimum_distance();
}

fn minimum_distance() {
    let nums = vec![1, 2, 3, 4, 5];
    let target = 5;
    let start = 3;
    let result = Solution::get_min_distance(nums, target, start);
    println!("result: {}", result);
}