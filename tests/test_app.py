import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest


def test_header_present(dash_duo):
    from app import app
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text is not None


def test_visualisation_present(dash_duo):
    from app import app
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#example-graph-2")
    assert graph is not None


def test_region_picker_present(dash_duo):
    from app import app
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-radio")
    assert radio is not None
