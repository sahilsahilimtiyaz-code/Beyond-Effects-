#!/usr/bin/env python3
# smali_check.py - lightweight static checks for hand-edited smali files
# usage: python3 smali_check.py file1.smali [...]
import re, sys

def check(path):
    text = open(path, encoding="utf-8").read()
    errs = []

    # split methods
    for m in re.finditer(r'(?m)^\.method\b.*$', text):
        start = m.start()
        endm = re.search(r'(?m)^\.end method\s*$', text[start:])
        if not endm:
            errs.append("method without .end: %s" % m.group(0)[:70])
            continue
        body = text[start:start + endm.end()]
        name = m.group(0)[:70]
        lm = re.search(r'\.locals\s+(\d+)', body)
        if lm:
            nloc = int(lm.group(1))
            for vm in re.finditer(r'\bv(\d+)\b', body):
                idx = int(vm.group(1))
                if idx >= nloc:
                    errs.append("register v%d >= .locals %d in %s" % (idx, nloc, name))
                    break
        # labels
        defined = set(re.findall(r'(?m)^\s*:([A-Za-z0-9_]+)\s*$', body))
        used = set()
        for um in re.finditer(r'(?m)^\s*(?:goto|if-[a-z0-9]+)\s+[^:\n]*?:([A-Za-z0-9_]+)', body):
            used.add(um.group(1))
        for cm in re.finditer(r'\.catch\s+\S+\s+\{[^}]*\}\s+:([A-Za-z0-9_]+)', body):
            used.add(cm.group(1))
        miss = used - defined
        if miss:
            errs.append("missing labels %s in %s" % (sorted(miss), name))
    # balanced directives
    if text.count(".method") != text.count(".end method"):
        errs.append("method/end-method count mismatch")
    # array-data sanity
    for am in re.finditer(r'\.array-data\s+\d+', text):
        seg = text[am.start():am.start() + 800]
        if ".end array-data" not in seg:
            errs.append("array-data without end near offset %d" % am.start())
    return errs

bad = 0
for p in sys.argv[1:]:
    errs = check(p)
    if errs:
        bad = 1
        print("FAIL", p)
        for e in errs:
            print("   ", e)
    else:
        print("OK  ", p)
sys.exit(bad)
