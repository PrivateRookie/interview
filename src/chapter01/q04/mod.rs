fn anagram(s: String, t: String) -> bool {
    s == t.chars().rev().collect::<String>()
}

#[test]
fn c1_q4_case1() {
    assert_eq!(anagram("abcd".to_string(), "dcba".to_string()), true);
}

#[test]
fn c1_q4_case2() {
    assert_eq!(anagram("abcd".to_string(), "dbca".to_string()), false);
}

#[test]
fn c1_q4_case3() {
    assert_eq!(anagram("".to_string(), "".to_string()), true);
}
