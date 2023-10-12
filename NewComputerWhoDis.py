import os
import subprocess

# List Applications from /Applications folder
application_folder = '/Applications'
applications = os.listdir(application_folder)
print('Applications:')
for app in applications:
    print(f'- {app}')

# Check programming language versions
languages = ['python', 'python3', 'ruby', 'node', 'perl', 'java', 'php']
print('\nProgramming Language Versions:')
for lang in languages:
    try:
        # Version information by using --version
        version_info = subprocess.check_output([lang, '--version'], stderr=subprocess.STDOUT)
        version_info = version_info.decode('utf-8').strip()
        print(f'- {version_info}')
    except Exception as e:
        print(f'- {lang} is not installed')
