import pytest


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        result = []
        for i, word in enumerate(words):
            if word[0].lower() not in ["a", "e", "i", "o", "u"]:
                word = word[1:] + word[:1]
            word += "ma"
            word += "a" * (i + 1)

            result.append(word)

        return " ".join(result)


@pytest.mark.parametrize(
    ("sentence", "expected"),
    [
        ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
        (
            "The quick brown fox jumped over the lazy dog",
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
        ),
    ],
)
def test_toGoatLatin(sentence: str, expected: str):
    assert Solution().toGoatLatin(sentence) == expected
