#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Some question/response tests for the theyspentwhat application
Q_AND_A = [
  ("in Islington during May 2010?",
   u"London Borough of Islington spent £34,386,647.00 total during May 2010"),
  ("in Islington during 2010-05?",
   u"London Borough of Islington spent £34,386,647.00 total during May 2010"),
  ("in Islington during 5/2010???!?",
   u"London Borough of Islington spent £34,386,647.00 total during May 2010"),
  ("in Islington during 2010",
   u"London Borough of Islington spent £100,499,424.37 total during 2010"),
  
  ("cambridgeshire",
  u"Cambridgeshire County Council spent £94,335,430.63 total during 2010"),
  ("cambridgeshire east",
  u"East Cambridgeshire spent £752,434.03 total during 2010"),
  ("in Cambridgeshire county during 2010-08?",
  u"Cambridgeshire County Council spent £49,983,826.78 total during Aug 2010"),
  
  ("in Cambridgeshire with the during 2010-08?",
  u"Cambridgeshire County Council spent £405,508.76 with The Mcavoy Group Limited during Aug 2010"),
  
  ("with the",
  u"The UK local government spent £74,719,194.68 with THE PRUDENTIAL ASSURANCE CO LIMITED during 2010"),
  ("with ltd",
  u"The UK local government spent £40,555,751.29 with RINGWAY JACOBS LTD during 2010"),
  
  ("brent with capita",
  u"London Borough of Brent spent £63,880.52 with CAPITA BUSINESS SERVICES LIMITED during 2010"),
]

# User details for the fake Twitter user used for tests
TEST_USER = {"id_str":"1234","screen_name":"test"}

import json
import os
import subprocess

# The WDDS root directory is the parent of the directory this script is in
WDDS_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
WDDS_BIN = os.path.join(WDDS_ROOT, "bin")

def main():
  proc = subprocess.Popen(
    os.path.join(WDDS_BIN, "theyspentwhat"),
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
  )
  
  failed_tests, passed_tests, n = 0, 0, 0
  for q, expected_answer in Q_AND_A:
    n += 1
    print >>proc.stdin, json.dumps({
      "user": TEST_USER,
      "id_str": str(n),
      "text": "@theyspentwhat " + q
    })
    actual_answer = json.loads(proc.stdout.readline())["status"]
    if actual_answer == "@%s %s" % (TEST_USER["screen_name"], expected_answer):
      passed_tests += 1
    else:
      failed_tests += 1
      print "Failed test %d" % n
      print "  got: " + actual_answer
      print "  expected: " + expected_answer
  
  print "Passed %d/%d tests" % (passed_tests, n)
  return 0 if passed_tests == n else 1

if __name__ == "__main__":
  exit(main())