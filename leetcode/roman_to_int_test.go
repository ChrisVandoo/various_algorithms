package leetcode

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

var tests = []struct {
	input    string
	expected int
}{
	{
		input:    "III",
		expected: 3,
	},
	{
		input:    "LVIII",
		expected: 58,
	},
	{
		input:    "MCMXCIV",
		expected: 1994,
	},
}

func TestRomanToInt(t *testing.T) {
	for _, test := range tests {
		res := RomanToInt(test.input)
		assert.Equal(t, test.expected, res, fmt.Sprintf("Failure for input: %s", test.input))
	}
}
