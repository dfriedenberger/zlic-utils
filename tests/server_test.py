from zlicutils.server import Server


def test_01():
    server = Server(host='0.0.0.0', port=8000)
    assert server._health()['Status'] == "UP"
