use std::collections::HashSet;
use std::mem;

use super::LinkList;

fn delete_duplicates(mut link: LinkList) -> LinkList {
    let mut unique_data = HashSet::new();
    let mut node = &mut link.head;
    while node.is_some() {
        if unique_data.contains(&node.as_ref().unwrap().data) {
            let temp = node.take();
            mem::swap(node, &mut temp.unwrap().next)
        } else {
            unique_data.insert(node.as_ref().unwrap().data);
            node = &mut node.as_mut().unwrap().next;
        }
    }
    link
}

#[test]
fn c2_q1_extra_test_equal() {
    let l = LinkList::from_vec(vec![1, 2, 3, 4]);
    let r = LinkList::from_vec(vec![1, 2, 3, 4]);
    assert_eq!(l, r);
}

#[test]
fn c2_q1_extra_test_not_equal() {
    let l = LinkList::from_vec(vec![1, 2, 3, 4]);
    let r = LinkList::from_vec(vec![1]);
    assert_eq!(l == r, false);
}

#[test]
fn c2_q1_case1() {
    let mut source = LinkList::from_vec(vec![1, 2, 3, 2]);
    let target = LinkList::from_vec(vec![1, 3, 2]);
    source = delete_duplicates(source);
    assert_eq!(source, target);
}

#[test]
fn c2_q1_case2() {
    let mut source = LinkList::from_vec(vec![1, 2, 3, 2, 3]);
    let target = LinkList::from_vec(vec![1, 2, 3]);
    source = delete_duplicates(source);
    assert_eq!(source, target);
}
