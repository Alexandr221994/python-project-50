from gendiff.scripts.gendiff import generate_diff


EXPECTED_JSON = "{\n  - follow: false\n  host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"


def test_gendiff():
    result_string = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')

    assert result_string == EXPECTED_JSON
