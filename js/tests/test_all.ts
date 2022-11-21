import {euler1} from "../puzzles/euler1"
import {euler2} from "../puzzles/euler2";

var assert = require('assert');

describe("puzzles", () => {
    [
        [euler1, 233168],
        [euler2, 4613732],
    ].forEach(([f, expected]: [() => number, number]) => {
        it(`${f.name}`, () => {
            assert.equal(f(), expected)
        })
    })
})