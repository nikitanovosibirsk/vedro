from pathlib import Path

import pytest

from vedro._core._scenario_loader import ScenarioFileLoader


@pytest.mark.asyncio
async def test_scenario_file_loader(tmp_path: Path):
    path = tmp_path / "scenario.py"
    path.write_text("\n".join([
        "import vedro",
        "class Scenario(vedro.Scenario):",
        "    pass",
    ]))

    loader = ScenarioFileLoader()
    scenarios = await loader.load(path)
    assert len(scenarios) == 1


@pytest.mark.asyncio
async def test_template_scenario_file_loader(tmp_path: Path):
    path = tmp_path / "scenario.py"
    path.write_text("\n".join([
        "import vedro",
        "class Scenario(vedro.Scenario):",
        "    @vedro.params('Bob')",
        "    @vedro.params('Alice')",
        "    def __init__(self, username):",
        "        pass",
    ]))

    loader = ScenarioFileLoader()
    scenarios = await loader.load(path)
    assert len(scenarios) == 2