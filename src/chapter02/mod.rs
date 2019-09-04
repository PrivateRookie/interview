use std::fmt::{Display, Formatter, Result};

pub mod q01;
pub mod q02;

#[derive(Debug)]
struct LinkList {
    head: Link,
}

type Link = Option<Box<Node>>;

#[derive(Debug)]
struct Node {
    data: i32,
    next: Link,
}

impl Display for Node {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        write!(f, "<Node {}>", self.data)
    }
}

impl LinkList {
    fn new() -> LinkList {
        LinkList { head: None }
    }

    fn from_vec(source: Vec<i32>) -> LinkList {
        let mut new_list = LinkList::new();
        for i in source {
            new_list.push(i)
        }
        new_list
    }

    fn push(&mut self, data: i32) {
        let new_node = Box::new(Node {
            data,
            next: self.head.take(),
        });
        self.head = Some(new_node);
    }
}

impl PartialEq for LinkList {
    fn eq(&self, other: &LinkList) -> bool {
        let mut equal = true;
        let (mut left, mut right) = (self.head.as_ref(), other.head.as_ref());
        loop {
            match (left, right) {
                (None, None) => break,
                (Some(l), Some(r)) => {
                    if l.data != r.data {
                        equal = false;
                        break;
                    } else {
                        left = l.next.as_ref();
                        right = r.next.as_ref();
                    }
                }
                _ => {
                    equal = false;
                    break;
                }
            }
        }
        equal
    }
}
