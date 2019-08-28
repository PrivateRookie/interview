// NOTE use "!" to represent null
fn reverse_str(s: String) -> String {
    s.chars().rev().skip(1).collect::<String>() + "!"
}

#[test]
fn c1_q2_case1() {
    assert_eq!(reverse_str("abcd!".to_string()), "dcba!".to_string());
}
#[test]
fn c1_q2_case2() {
    assert_eq!(reverse_str("!".to_string()), "!".to_string());
}
