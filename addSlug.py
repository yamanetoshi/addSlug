#!/usr/bin/env python

import sys
import frontmatter
import os
import re

def main():
    args = sys.argv
    filename = args[1]

    basestring = os.path.splitext(os.path.basename(filename))[0]
    result = re.sub(r'^\d{4}-\d{1,2}-\d{1,2}-', "", basestring)

    with open(filename) as f:
        post = frontmatter.loads(f.read())

    post.metadata.update({'slug' : result})
    print(frontmatter.dumps(post))

if __name__ == "__main__":
    main()
