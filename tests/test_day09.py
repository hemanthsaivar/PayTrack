from unittest.mock import patch
from streamlit.testing.v1 import AppTest
from frontend.state import initialize_state

def test_filter_survives_rerun():
    fresh = {}
    initialize_state(fresh)
    assert fresh['show_paid_only'] is False
    with patch('frontend.client.call', return_value=[]):
        app = AppTest.from_file('frontend/app.py').run()
        assert not app.exception
        app.checkbox[0].check().run()
        assert not app.exception
        assert app.checkbox[0].value is True
        app.run()
        assert app.checkbox[0].value is True
