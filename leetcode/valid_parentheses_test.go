package leetcode

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

var vp_tests = []struct {
	input    string
	expected bool
}{
	{
		input:    "]",
		expected: false,
	},
	{
		input:    "()",
		expected: true,
	},
	{
		input:    "()[]{}",
		expected: true,
	},
	{
		input:    "([)]",
		expected: false,
	},
	{
		input:    "([])()()",
		expected: true,
	},
}

func TestValidParentheses(t *testing.T) {
	for _, test := range vp_tests {
		res := isValid(test.input)
		assert.Equal(t, test.expected, res, fmt.Sprintf("Failure for input: %s", test.input))
	}
}
