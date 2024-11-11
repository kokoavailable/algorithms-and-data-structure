impl Solution {
    pub fn reverse_words(s: String) -> String {
        s.split_whitespace()              // 1단계: `s`의 공백을 기준으로 단어를 분리 (불변)
            .rev()                         // 2단계: iterator의 순서를 뒤집음 (불변)
            .collect::<Vec<&str>>()        // 3단계: `Vec<&str>`로 수집 (가변)
            .join(" ")                     // 4단계: 문자열로 결합하여 반환
    }
}