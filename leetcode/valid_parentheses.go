package leetcode

/*
Rules:
- open bracket must be closed by matching bracket
- every close bracket must have a matching open bracket
- brackets must be closed in order - i think that means something like [{]} would be illegal...

Thoughts:
- loop through the string, need a way to track what type of bracket we are looking for
- if can't be in weird order does that mean we can loop in from both ends of the string? no ()[] is valid
- inneficiant solution: start at beginning, find bracket, loop through string to see if we can get a match,
  if not, invalid, if we do, move on to the next bracket...

- can i do something clever converting string -> map with indexes?
- if i get bracket, search for opposing bracket?

- or is this some kind of recursive nonsense?

Some possible cases:
()}
[{()}]
{}[]
*/

func match(r rune) rune {
	switch r {
	case ')':
		return '('
	case ']':
		return '['
	case '}':
		return '{'
	}
	return rune(0)
}

func isValid(s string) bool {
	bracketQueue := []rune{}

	for _, b := range s {
		if b == '}' || b == ']' || b == ')' {
			latest := len(bracketQueue) - 1
			matchingOpenBracket := match(b)

			if latest >= 0 && matchingOpenBracket == bracketQueue[latest] {
				bracketQueue = bracketQueue[:latest]
			} else {
				// we've found an unexpected closing bracket which makes this string invalid ex. [}]
				return false
			}
		} else {
			bracketQueue = append(bracketQueue, b)
		}
	}

	if len(bracketQueue) == 0 {
		return true
	} else {
		return false
	}
}
