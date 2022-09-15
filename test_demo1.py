import pytest

def f():
    raise SystemExit

class TestSuite:
    def test_tc_001(self):
        with pytest.raises(SystemExit):
            f()

    def test_tc_002(self, tmp_path):
        print(tmp_path)
        assert 0

    def test_tc_003(self):
        with pytest.raises(RuntimeError) as exeinfo:
            def f():
                f()
            f()
        assert "maximum recursion" in str(exeinfo.value)