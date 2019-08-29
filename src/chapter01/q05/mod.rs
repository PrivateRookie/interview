fn replace(s: String) -> String {
    s.chars()
        .map(|ch| match ch {
            ' ' => String::from("02%"),
            c @ _ => c.to_string(),
        })
        .collect::<String>()
}

#[test]
fn c1_q5_case1() {
    assert_eq!(replace("ab d".to_string()), "ab02%d".to_string());
}

#[test]
fn c1_q5_case2() {
    assert_eq!(replace(" abc".to_string()), "02%abc");
}

#[test]
fn c1_q5_case3() {
    assert_eq!(replace("abc ".to_string()), "abc02%");
}
