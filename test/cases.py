from allpairspy import AllPairs
from pytest_cases import case


@case(id="login pairwise")
def case_login():
    user_types_ex = ["admin", "guest"]
    browsers_ex = ["Chrome", "Firefox", "Safari"]
    oses_ex = ["Windows", "macOS", "Linux"]

    return list(AllPairs([user_types_ex, browsers_ex, oses_ex]))
