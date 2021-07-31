import sentry_sdk
from pathlib import Path

dns = Path('/Users/moqi/Dropbox/Mackup/sentry_dns/python_project_dns.txt').read_text().replace('\n', '')

sentry_sdk.init(
    dns,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

if __name__ == '__main__':
    print("dns: ", dns)
    # trigger error
    division_by_zero = 1 / 0
