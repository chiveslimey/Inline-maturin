import maturin_utils

def test_build():

    # ビルド
    maturin_utils.build_maturin_project('pymodtest')

    # 関数のチェック
    import pymodtest
    assert pymodtest.add_two(6) == 8

    return
