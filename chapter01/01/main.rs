use std::collections::HashMap;

fn unique_char_map(s: String) -> bool {
    let mut char_map: HashMap<char, usize> = HashMap::new();
    for c in s.chars() {
        match char_map.get_mut(&c) {
            Some(count) => *count += 1,
            None => {
                char_map.insert(c, 1);
            }
        }
    }
    char_map.values().all(|count| count <= &1)
}

fn unique_char_vec(s: String) -> bool {
    let mut char_vec = [0; 128];
    let mut unique = true;
    // this work for ascii code only
    for c in s.bytes().map(|c| c as usize) {
        char_vec[c] += 1;
        if char_vec[c] > 1 {
            unique = false;
            break;
        }
    }
    unique
}

fn main() {
    assert_eq!(unique_char_map("abcd".to_string()), true);
    assert_eq!(unique_char_map("aabcd".to_string()), false);
    assert_eq!(unique_char_vec("abcd".to_string()), true);
    assert_eq!(unique_char_vec("aabcd".to_string()), false);
     assert_eq!(unique_char_vec("aAbcd".to_string()), true);
}
