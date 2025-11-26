# algorithms/railfence.py

def encrypt(text, rails):
    text = text.replace(" ", "")  # optional: remove spaces
    fence = [[] for _ in range(rails)]

    rail = 0
    direction = 1  # 1 = down, -1 = up

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    encrypted = "".join("".join(row) for row in fence)
    return encrypted


def decrypt(ciphertext, rails):
    # Build the zig-zag pattern
    fence = [[] for _ in range(rails)]
    pattern = []
    rail = 0
    direction = 1

    for _ in ciphertext:
        pattern.append(rail)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Fill the rails
    rail_lengths = [pattern.count(r) for r in range(rails)]
    index = 0
    for r in range(rails):
        fence[r] = list(ciphertext[index:index + rail_lengths[r]])
        index += rail_lengths[r]

    # Read in zig-zag order
    result = []
    rail_index = [0] * rails

    for r in pattern:
        result.append(fence[r][rail_index[r]])
        rail_index[r] += 1

    return "".join(result)