import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import app


class FakeTable:
    def update_item(self, **kwargs):
        assert kwargs["Key"] == {"id": "visitor_count"}
        assert kwargs["UpdateExpression"] == "ADD #count :incr"
        assert kwargs["ExpressionAttributeNames"] == {"#count": "count"}
        assert kwargs["ExpressionAttributeValues"] == {":incr": 1}
        return {"Attributes": {"count": 42}}


def test_lambda_handler_increments_counter(monkeypatch):
    monkeypatch.setattr(app, "get_table", lambda: FakeTable())

    result = app.lambda_handler({}, {})

    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert body["count"] == 42
    assert result["headers"]["Access-Control-Allow-Origin"] == "*"
