# wget https://github.com/ec-jrc/lisflood-code/archive/ddaef5a.zip
import os
import sys
import zipfile
from urllib import request


def main():
    with open('./commits_to_test.txt') as fh:
        commits = fh.readlines()

    readme_comment = ''
    i = 1
    for c in commits:
        c = c.strip()
        if not c:
            continue
        if c.startswith('#'):
            readme_comment = c
            continue
        commit = c[:8]
        path_to_archive = os.path.join('/workarea/lisflood_versions', f'{i}_{commit}.zip')
        print(readme_comment)
        print('Downloading...', commit)
        request.urlretrieve(f'https://github.com/ec-jrc/lisflood-code/archive/{commit}.zip', filename=path_to_archive)
        with zipfile.ZipFile(path_to_archive, 'r') as zip_ref:
            zip_ref.extractall(f'/workarea/lisflood_versions/{i}_{commit}/')
            print('[+] Extracting to ', f'/workarea/lisflood_versions/{i}_{commit}/')
            if readme_comment:
                with open(f'/workarea/lisflood_versions/{i}_{commit}/COMMENT.md', 'w') as f:
                    f.write(readme_comment + '\n')
                readme_comment = ''
            i += 1



if __name__ == '__main__':
    sys.exit(main())
