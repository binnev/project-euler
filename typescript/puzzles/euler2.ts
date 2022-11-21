export function euler2(): number {
    const N = 4e6
    let [a, b, c] = [1, 2, 0]
    let evenSum = b
    while (c <= N) {
        c = a + b
        a = b
        b = c
        if (c % 2 == 0){
            evenSum += c
        }
    }
    return evenSum
}