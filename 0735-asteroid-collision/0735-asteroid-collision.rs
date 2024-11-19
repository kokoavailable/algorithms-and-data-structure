impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<i32> = Vec::new();

        for &aster in &asteroids {
            let mut collided = false;

            while let Some(&last) = stack.last() {
                if last > 0 && aster < 0 {
                    if last.abs() < aster.abs() {
                        stack.pop();
                        continue
                    } 
                    else if last.abs() == aster.abs() {
                        stack.pop(); // 둘 다 폭발
                    }
                    collided = true; // 충돌 발생
                    break;
                } else {
                    break; // 충돌 조건이 아니므로 루프 종료
                }
            }

            if !collided {
                stack.push(aster); // 충돌하지 않은 경우 현재 행성을 스택에 추가
            }
        }

        stack
    }
}