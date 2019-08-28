fn remove_duplicates(s: String) -> String {
    if s.len() < 2 {
        s
    } else {
        let mut result = vec![];
        for ch in s.chars() {
            if result.contains(&ch) {
                continue;
            } else {
                result.push(ch)
            }
        }
        result.into_iter().collect::<String>()
    }
}

#[test]
fn c1_q3_case1() {
    assert_eq!(remove_duplicates("abcd".to_string()), "abcd".to_string());
}
#[test]
fn c1_q3_case2() {
    assert_eq!(remove_duplicates("aaaa".to_string()), "a".to_string());
}
#[test]
fn c1_q3_case3() {
    assert_eq!(remove_duplicates("".to_string()), "".to_string());
}
#[test]
fn c1_q3_case4() {
    assert_eq!(remove_duplicates("aabbcc".to_string()), "abc".to_string());
}

