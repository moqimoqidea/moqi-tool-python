import os
import re
import threading
from datetime import datetime

import requests

artifact_url = 'https://repo.maven.apache.org/maven2/com/google/guava/guava/21.0/'
request_params = {'proxies': 'http://127.0.0.1:6152'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
resource_reg = re.compile(r'<a href="(.*?)" title="\1">')


def download_file(file_dir, url):
    local_filename = url.split('/')[-1]
    print('%s: downloading %s start' % (datetime.now(), local_filename))

    with requests.get(url,
                      params=request_params,
                      headers=headers,
                      stream=True,
                      allow_redirects=True) as r:
        r.raise_for_status()
        with open(file_dir + '/' + local_filename, 'wb') as f:
            for chunk in r.iter_content(100000):
                f.write(chunk)

    print('%s: downloading %s end' % (datetime.now(), local_filename))


if __name__ == '__main__':
    os.chdir('../maven_repo')
    maven_repo_dir = os.getcwd()
    print('maven_repo_dir is %s' % maven_repo_dir)

    artifact_html_text = requests.get(artifact_url, params=request_params, headers=headers).text
    all_resources = re.findall(resource_reg, artifact_html_text)
    print('all resources is %s\n' % all_resources)

    downloadThreads = []
    for resource in all_resources:
        downloadThread = threading.Thread(target=download_file, args=(maven_repo_dir, artifact_url + resource))
        downloadThreads.append(downloadThread)
        downloadThread.start()

    for downloadThread in downloadThreads:
        downloadThread.join()

    print('\nall done!')
