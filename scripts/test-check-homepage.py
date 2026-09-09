"""Regression scenarios for the homepage integrity checker (standard library only)."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile

sys.dont_write_bytecode = True
root=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('homepage_check',root/'scripts/check-homepage.py')
module=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=module
spec.loader.exec_module(module)
source=(root/'index.html').read_text()
fixtures=json.loads((root/'scripts/homepage-reference.json').read_text())
cases={
    'valid homepage':(source,0),
    'placeholder link':(source.replace('href="https://arxiv.org/abs/2605.00809"','href="coming soon"'),1),
    'missing image':(source.replace('src="static/images/genlip-overview.png"','src="static/images/missing.png"').replace('src="static/images/genlip-overview.webp"','src="static/images/missing.webp"'),1),
    'incorrect benchmark':(source.replace('<td>73.6</td>','<td>99.9</td>'),1),
    'missing visible BAAI':(source.replace('<span><sup>4</sup> Beijing Academy of Artificial Intelligence</span>',''),1),
    'incorrect author affiliation':(source.replace('Yunchao Wei</a><sup>1,4,&dagger;','Yunchao Wei</a><sup>1,&dagger;'),1),
}
for label,(html,expected) in cases.items():
    if expected:assert html!=source,label
    with tempfile.TemporaryDirectory(prefix='genlip-check-') as directory:
        test=Path(directory)
        (test/'scripts').mkdir()
        (test/'scripts/homepage-reference.json').write_text(json.dumps(fixtures))
        (test/'index.html').write_text(html)
        (test/'static').symlink_to(root/'static',target_is_directory=True)
        module.ROOT=test
        with contextlib.redirect_stdout(io.StringIO()):actual=module.check()
        print(f'{label}: returned {actual}, expected {expected}')
        assert actual==expected,label
print('All six checker regression scenarios passed.')
