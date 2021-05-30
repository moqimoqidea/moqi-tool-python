import os
import re

import requests

if __name__ == '__main__':
    os.chdir('../maven_repo')
    maven_repo_dir = os.getcwd()
    print('maven_repo_dir is %s' % maven_repo_dir)

    maven_center_repo = 'https://repo.maven.apache.org/maven2'
    url = maven_center_repo + '/com/google/guava/guava/21.0/'
    request_params = {'proxies': 'http://127.0.0.1:6152'}

    resource_reg = re.compile(r'<a href="(.*?)" title="\1">')
    all_resources = re.findall(resource_reg, requests.get(url, params=request_params).text)
    print('all resources is %s' % all_resources)

    for resource in all_resources:
        print('download %s start' % resource)
        open(maven_repo_dir + '/' + resource, 'wb').write(requests.get(url + resource, params=request_params).content)
        print('download %s end' % resource)

    print('all done!')
