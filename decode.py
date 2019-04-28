import base64
import re
data = '5Crs9ebUmRoC9xKwKGhqJWrA2Xoa9qKwKG2H+WKiKRo4E6mGKGpq+GNqJWrsukIcuk/7EaDS9kBqvqrG9aUH26FsmErS2ydHmR7imkXS9Rb8mEKqJWrS2yMf/RQqvqKtJGdqJWrS2yMf/R+qvGhiKRrCukDTKGpq2abP26FHmCKiKRXAmeFiKGpqBUUPN4Bs+ndqJWr4u6r7mkQqvqKt+njs0GhsvndqJWrHmEO696rcE6OD2eBqvqKP+qKiKRXHuCKwKqKiKRXGuCKwKqKiKRtS9R/Xuk/7KGpq5RjqJWrUlkX75RoHmxKwKT/IFWisvnps+WKiK8ITlXoamEKqvqrFNFg4JGKH+WKiKR/sE6m72qKwKGhCJGBH+3BPuktiKbisExM9Bbr/KnKtv3NQI3T6vxKiK8FSKGpq3kowlktiuFsAIxQsKWS+lkDX5nijNkDT2RoZmWd6JGd1KbIIJB+X+ndsKhrXlktTEWovBTND+hU1Ky/a0xMM2yMimF/7uTPZ/bsAI3+6JG+aKWSJxbOI3Wsj9e7cmxMymkIc9CTjFRFC2a7A97sAIWQsKhIp2RoPmFsAIGBH+WQ4+4KXJGhsvxMI9arZ9eBjBabRuErZEWgX+42H+4uqJWrA2R7798NqvGhiK8ID26O79xKw+xsq98/f/RFCKGpqKqsquEMsEa7TKGpqu3FSu3bRvkO7mehCIRNqJWrs9boZmWKwKRKXukhtmRhU+3uXmkh4Kqsq2RFtEa7TKGpq5EFROahsOxi6N77cBF+UOhbPl3I3+UZD+GMaIR7mxaiDxXOtFbmFkbIJ+e2a/n7KIatPNEmV0UPL5nSnKWPKEWoK3BrJ3RTtlRbeFX7XkFSM/y7UkTpcIRIUx4meIRr6OaSbxGF73eo7NRSh9XF2J6/RBEOe/TSrN3uUKe7D3RK438hQ2R7s3bOD3eINB3/l58bJ9BD85eIeu6rP9B2a/eFm3ePXBRoMm7haF6ht3F7kuFFSuT7ZBxMR06u4+F/A2U77vbsAkBXm3TDVkRmT9nrlmhF33GrVlF+U3hSrkBSbvBPb5BtxNkut/TOL/kXpl4UqJWrU5EM7KGp4JWrXmXoZmWKwKGBQ+xKiKRD6EamZ2RXflkNqvGhiK8IGE6OD2eBqvqKsKqsqm6rAEa7TKGpq+4NqJWrR96rPuENqvqKsKqsq2yrAm6r726+qvGdiKRFQ/yrSKGZ1K8OZ/et7KGpqKqsq2eP83RbPmxKwKqKiKRbs2bIZ5RBqvqKqJWr728rA2TIAmeBqvqKt+ndsKqsqmErC96rI2a2qvqrVuEmS5WDHmENH26IiJ7I33hSS9RO4lebcmBFQuaFs/e7A9GpjlRbauxD4mkIX2R7U5xDGmErUJTI728ONuEOpFRbilkOS/eoCOESGmEMUlkoHvqMB28F4/WMS9RIp96KjmRoCKeI728OZmR7GuEOZ9aQj2ebUlWMH96NjmRoX9RNHK8Xo'


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


def upEncode(data):
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    CHARS1 = 'dMWnhbeyKr0J+IvLNOx3BFkEuml92/5fjSqGT7R8pZVciPHAstC4UXa6QDw1gozY'
    str = base64.b64encode(data.encode(encoding="utf-8"))
    str = multiple_replace(data, dict(zip(CHARS1, CHARS)))
    str = base64.b64decode(str).decode()
    return str

print(upEncode(data))
