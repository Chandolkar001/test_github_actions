from tabulate import tabulate

data = [
  {
    'data': [
      {
        'commitHash': '123456',
        'branch': 'main',
        'message': 'User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities',
        'path': 'test.js',
        'lines': "document.write('<p>' + userInputXSS + '</p>');",
        'engine': 'OSS',
        'vulnerabilityClass': [
          'A07:2017 - Cross-Site Scripting (XSS)',
          'A03:2021 - Injection'
        ],
        'start': {
          'col': 1,
          'line': 15,
          'offset': 407
        },
        'end': {
          'col': 46,
          'line': 15,
          'offset': 452
        },
        'codeBlock': "// Example 3: XSS (Cross-Site Scripting)\nconst userInputXSS = process.argv[4];\ndocument.write('<p>' + userInputXSS + '</p>');\n\n// Example 4: Insecure Password Handling\n"
      }
    ],
    'rule': 'github_javascript.browser.security.insecure-document-method.insecure-document-method',
    'status': 'success',
    'result': 'failure'
  },
  {
    'data': [
      {
        'commitHash': '123456',
        'branch': 'main',
        'message': 'It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as bcrypt. You can use the `bcrypt` node.js package.',
        'path': 'test.js',
        'lines': "const weakHash = (password) => crypto.createHash('md5').update(password).digest('hex');",
        'engine': 'OSS',

        'start': {
          'col': 29,
          'line': 23,
          'offset': 693
        },
        'end': {
          'col': 87,
          'line': 23,
          'offset': 751
        },
        'codeBlock': "// Example 5: Use of weak cryptographic function\nconst crypto = require('crypto');\nconst weakHash = (password) => crypto.createHash('md5').update(password).digest('hex');\nconst userPasswordHashed = process.argv[6];\nconsole.log('Hashed Password:', weakHash(userPasswordHashed));\n"
      }
    ],
    'rule': 'github_javascript.lang.security.audit.md5-used-as-password.md5-used-as-password',
    'status': 'success',
    'result': 'failure'
  }
]

def print_table_for_vs(data):
    table_data = []
    for item in data:
        vulnerability_data = item.get('data', [])

        # Check if data is not an empty list and has at least one element
        if vulnerability_data:
            vulnerability = vulnerability_data[0]

            commit_hash = vulnerability.get('commitHash', 'N/A')
            branch = vulnerability.get('branch', 'N/A')
            path = vulnerability.get('path', 'N/A')
            message = vulnerability.get('message', 'N/A')
            vclass = ', '.join(vulnerability.get('vulnerabilityClass', []))
            rule = item.get('rule', 'N/A')
            status = item.get('status', 'N/A')
            result = item.get('result', 'N/A')

            table_data.append([commit_hash, branch, path, message, vclass, rule, status, result])
        else:
            # Handle the case where 'data' key is not present or is an empty list
            table_data.append(['N/A'] * 8)


    headers = ['Commit Hash', 'Branch', 'Path', 'Message', 'Vulnerability Class', 'Rule', 'Status', 'Result']
    max_col_width = 30
    print(tabulate(table_data, headers=headers, tablefmt='grid', maxcolwidths=max_col_width))
    

print_table_for_vs(data)
