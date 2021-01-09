encoded_msg = "1c41023f564b2a130824570e6b47046b521f3f5208201318245e0e6b40022643072e13183e51183f5a1f3e4702245d4b285a1b23561965133f2413192e571e28564b3f5b0e6b50042643072e4b023f4a4b24554b3f5b0238130425564b3c564b3c5a0727131e38564b245d0732131e3b430e39500a38564b27561f3f5619381f4b385c4b3f5b0e6b580e32401b2a500e6b5a186b5c05274a4b79054a6b67046b540e3f131f235a186b5c052e13192254033f130a3e470426521f22500a275f126b4a043e131c225f076b431924510a295f126b5d0e2e574b3f5c4b3e400e6b400426564b385c193f13042d130c2e5d0e3f5a086b52072c5c192247032613433c5b02285b4b3c5c1920560f6b47032e13092e401f6b5f0a38474b32560a391a476b40022646072a470e2f130a255d0e2a5f0225544b24414b2c410a2f5a0e25474b2f56182856053f1d4b185619225c1e385f1267131c395a1f2e13023f13192254033f13052444476b4a043e131c225f076b5d0e2e574b22474b3f5c4b2f56082243032e414b3f5b0e6b5d0e33474b245d0e6b52186b440e275f456b710e2a414b225d4b265a052f1f4b3f5b0e395689cbaa186b5d046b401b2a500e381d4b23471f3b4051641c0f2450186554042454072e1d08245e442f5c083e5e0e2547442f1c5a0a64123c503e027e040c413428592406521a21420e184a2a32492072000228622e7f64467d512f0e7f0d1a"
bytes_object = bytes.fromhex(encoded_msg)
ascii_msg = bytes_object.decode(encoding='ascii', errors='ignore')

def decode(message, key):
    repeated_key = key * (len(message) // len(key) + 1)
    return ''.join(chr(ord(char) ^ ord(r_key)) for char, r_key in zip(message, repeated_key))

def get_ioc_states(decoded_msg):
    ioc_dict = [1] * len(decoded_msg)
    shift = 1
    while shift != len(decoded_msg):
        ioc = 0
        shifted_msg = decoded_msg[shift:] + decoded_msg[:shift]
        for i in range(len(decoded_msg)):
            if shifted_msg[i] == decoded_msg[i]:
                ioc += 1
        ioc_dict[shift] = ioc / len(decoded_msg)
        shift += 1
    return ioc_dict

# We have a peak value for every third element - assuming that KEY_LENGTH is 3
# print(get_ioc_states(bytes_object))

# https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f
letterFrequency = {
    'E' : 12.0,
    'T' : 9.10,
    'A' : 8.12,
    'O' : 7.68,
    'I' : 7.31,
    'N' : 6.95,
    'S' : 6.28,
    'R' : 6.02,
    'H' : 5.92,
    'D' : 4.32,
    'L' : 3.98,
    'U' : 2.88,
    'C' : 2.71,
    'M' : 2.61,
    'F' : 2.30,
    'Y' : 2.11,
    'W' : 2.09,
    'G' : 2.03,
    'P' : 1.82,
    'B' : 1.49,
    'V' : 1.11,
    'K' : 0.69,
    'X' : 0.17,
    'Q' : 0.11,
    'J' : 0.10,
    'Z' : 0.07 
}

def get_distribution(msg):
    distribution = {}
    for char in msg:
        if not char in distribution:
            distribution[char] = 0
        distribution[char] += 1
    return distribution


def split_to_repeated_sequences(text, key_len):
    return tuple(text[shift::key_len] for shift in range(key_len))


def get_chi_squared(distribution, msg_len):
    chi_squared_sum = 0
    for char, english_distribution in letterFrequency.items():
        expected_amount = english_distribution * msg_len / 100

        if char in distribution:
            actual_amount = distribution[char]
        elif char.lower() in distribution:
            actual_amount = distribution[char.lower()]
        else:
            actual_amount = 0

        chi_squared_sum += (actual_amount - expected_amount) ** 2 / expected_amount
    return chi_squared_sum

def get_key(encoded_msg, key_len):
    key = []
    for sequence in split_to_repeated_sequences(encoded_msg, key_len):
        statistics = {}
        for xor_key in range(256):
            decoded_sequence = decode(sequence, chr(xor_key))
            if not decoded_sequence:
                continue
            sequence_len = len(decoded_sequence)
            char_distribution = get_distribution(decoded_sequence)
            chi_squared = get_chi_squared(char_distribution, sequence_len)
            statistics[xor_key] = chi_squared
        key.append(min(statistics, key=lambda k: statistics[k]))
    return ''.join(chr(k) for k in key)


key = get_key(ascii_msg, 3)
print(decode(ascii_msg, key))