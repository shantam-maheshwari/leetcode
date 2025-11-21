from typing import List

import pytest


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        num_of_teams = len(skill) // 2
        total_skill = sum(skill)

        if total_skill % num_of_teams != 0:
            return -1

        skill_per_team = total_skill // num_of_teams

        chemistry = 0
        skill_counts = {}
        for s in skill:
            if s in skill_counts:
                if skill_counts[s] > 1:
                    skill_counts[s] -= 1
                else:
                    del skill_counts[s]
                chemistry += s * (skill_per_team - s)
            else:
                skill_counts[skill_per_team - s] = (
                    skill_counts.get(skill_per_team - s, 0) + 1
                )

        return chemistry if len(skill_counts) == 0 else -1


@pytest.mark.parametrize(
    ("skill", "expected"), [([3, 2, 5, 1, 3, 4], 22), ([3, 4], 12)]
)
def test_dividePlayers(skill: List[int], expected: int):
    assert Solution().dividePlayers(skill) == expected
