from repo2readme.utils.filter import github_file_filter


def test_github_file_filter_allows_valid_files():
    assert github_file_filter("repo2readme/cli/main.py") == True
    assert github_file_filter("src/app.tsx") == True

def test_github_file_filter_blocks_ignored_dirs():
    assert github_file_filter("node_modules/package/index.js") == False
    assert github_file_filter(".git/config") == False
    assert github_file_filter("venv/bin/activate") == False

def test_github_file_filter_blocks_ignored_extensions():
    assert github_file_filter("dist/app.exe") == False
    assert github_file_filter("data.csv") == False