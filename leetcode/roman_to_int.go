package leetcode

func RomanToInt(s string) int {
	var res int

	for index, symbol := range s {
		// Get next symbol (if it exists)
		var next byte
		if index+1 < len(s) {
			next = s[index+1]
		}

		// Get previous symbol (if it exists)
		var previous byte
		if index-1 >= 0 {
			previous = s[index-1]
		}

		switch symbol {
		case 'I':
			if next != 'V' && next != 'X' {
				res += 1
			}
		case 'V':
			if previous == 'I' {
				res += 4
			} else {
				res += 5
			}
		case 'X':
			if previous == 'I' {
				res += 9
			} else if next != 'L' && next != 'C' {
				res += 10
			}
		case 'L':
			if previous == 'X' {
				res += 40
			} else {
				res += 50
			}
		case 'C':
			if previous == 'X' {
				res += 90
			} else if next != 'D' && next != 'M' {
				res += 100
			}
		case 'D':
			if previous == 'C' {
				res += 400
			} else {
				res += 500
			}
		case 'M':
			if previous == 'C' {
				res += 900
			} else {
				res += 1000
			}
		}

	}
	return res
}
