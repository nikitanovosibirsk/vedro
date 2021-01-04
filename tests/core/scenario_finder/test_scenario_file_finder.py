from pathlib import Path
from typing import List

import pytest

from vedro._core._scenario_finder import ScenarioFileFinder


def _create_file_tree(tree: List[Path]) -> List[Path]:
    for path in tree:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("")
    return tree


@pytest.mark.asyncio
async def test_scenario_file_finder(tmp_path: Path):
    tree = _create_file_tree([
        (tmp_path / ".DS_Store"),
        (tmp_path / "scenario1.py"),
        (tmp_path / "scenario2.py"),
        (tmp_path / "folder1" / "scenario3.py"),
        (tmp_path / "folder1" / "__pychache__" / "scenario3.pyc"),
        (tmp_path / "folder2" / "__init__.py"),
        (tmp_path / "folder2" / "scenario4.py"),
        (tmp_path / "folder2" / "scenario5.py"),
        (tmp_path / "folder3" / "folder4" / "scenario6.py"),
        (tmp_path / "folder3" / "folder4" / "scenario6.pyc"),
    ])

    finder = ScenarioFileFinder()
    paths = []
    async for path in finder.find(tmp_path):
        paths.append(path)

    assert set(paths) == set(tree)
    assert len(paths) == len(tree)