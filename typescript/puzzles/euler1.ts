export function euler1(): number {
    const N = 1000
    let multiplesSum = 0
    for (var n = 0; n < N; n++) {
        if (n % 3 === 0 || n % 5 === 0) {
            multiplesSum += n
        }
    }
    return multiplesSum
}


// apparently this is the JS equivalent of if __name__ == "__main__"
if (require.main === module) {
    console.log(euler1())
}