fn rotate(matrix: [[usize; 5]; 5]) -> [[usize; 5]; 5] {
    let mut m = matrix;
    let size = m.len();
    for i in 0..size {
        for j in (i + 1)..size {
            let tmp = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = tmp;
        }
    }
    for i in 0..size {
        for j in 0..2 {
            let tmp = m[i][j];
            m[i][j] = m[i][4 - j];
            m[i][4 - j] = tmp;
        }
    }
    m
}

#[test]
fn c1_q6_case1() {
    let matrix: [[usize; 5]; 5] = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ];
    let target: [[usize; 5]; 5] = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ];
    assert_eq!(rotate(matrix), target);;
}
