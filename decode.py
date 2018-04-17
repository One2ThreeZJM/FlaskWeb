import base64
import re
data = '5Crs9ebUmRoC9xKwKGhqJWrA2Xoa9qKwKGjH+WQsKqsq96If/R+qvqKCIqKiK8MSuaPSmaFf9RbPmxKwKRIA9xDq9ao4/eFCJ8IX2eFCOeFP9CKiKRbs2boa9qKwKGhH+WKiKRbs2boauCKw+xsqu8rS9RNqvqr89ao89eBqJWrP9aO79WKwKTD75yF4KnmNKqsq2aICmkFHKGpq+3NU+WptInNsKqsq9RFU/aoClXoU5EM7KGpqJ3KqJWrP9R+qvqKqJWrPua+qvqKqJWriukD8/kb8mxKwK8ZpKqsq/e7PmEZA9RBqvqry3FNc+njw+ndqJWr4mePf/RFCKGpqFBbf+xQsKqsqm6Mf/RFCKGpqvxQtJGKUJkbi9WM9+bUjkXMxExdtvn2D+nhXIGhqJWrXuxKwKTXA5R7i9eb2J4BH+Wdp3e7H/Ej1KhbHmyrAlkNjvWQsJGd1KhD75yF4KnmNKhrXlktTEWoLBbKaJGh6+nuC+CQs+3T1Ky/a0xMM2yMimF/7uTPZ/bsAI3+6JG+aKWSJxbOI3Wsj9e7cmxMymkIc9CTjFRFC2a7A97sAIWQsKhIp2RoPmFsAIGKH+WQ4+GdCJGjUKhXAuR7imxM3ukmS2R72J4B4ICQ4IqKiKRoClkFH/WKw+xsquEMsEa7TKGpqIeu6uG7Su4h6meFGuG7qukr7u4j4ukbG+n2QI4NCu42qJWrs9boZmWKwKRKXukhtmRhXmnhs+3TsKqsq2yIflkNqvqKX+4hDInOG+WUCu4hUJ3htm3jPuGKt+WXTIaNUIkIGu4jX+k+qJWr4mEI4lkoHEa7TKGpqKqsq98/f/RFCKGpq5XsqmRbGmkrA9aP2KGZ2K7sqJbsqlkDP9arZEWKwEWK6JGdH+bsqJbsqukOP9ar2KGZ2K7sqJbsqmRtX28rDEWKwEWre9yFC287fNkDT2RoZmbgCI3OfvWQsJGr2Kqt2KRXAu8mZ26OSEWKwEWr2Kqt2KRbs2etA/R7HEWKwEWK6JGjHI7sqfxro'


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


def upEncode(data):
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    CHARS1 = 'dMWnhbeyKr0J+IvLNOx3BFkEuml92/5fjSqGT7R8pZVciPHAstC4UXa6QDw1gozY'
    str = base64.b64encode(data)
    str = multiple_replace(data, dict(zip(CHARS1, CHARS)))
    str = base64.b64decode(str)
    return str

upEncode(data)
