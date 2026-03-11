def joltage(inputText, k):
    jolts = list(inputText.strip())
    n = len(jolts)
    best = 0

    def pick(level, start_idx, current):
        nonlocal best

        if level == k:
            num_str = "".join(current)
            val = int(num_str)
            if val > best:
                best = val
            return

        # We still need (k - level) digits, so we cannot start too far to the right
        for idx in range(start_idx, n - (k - level) + 1):
            current.append(jolts[idx])
            pick(level + 1, idx + 1, current)
            current.pop()

    pick(0, 0, [])
    print(best)
    return best





file_path = "03/inp.txt"
answer = 0

with open(file_path, 'r') as file:
    for line in file:
        jolting = joltage(line.strip(),12)
        answer += jolting


print("Answer =", answer)