"""Finite, independently auditable checks for consolidation pass 2.

These checks validate explicit P009/P018 examples and the archival
cross-reference. They do NOT establish general conjectures or originality.
"""
from pathlib import Path
from itertools import combinations
import unittest

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/"audits/2026-10-29-P015-P016-P018-P020-source-comparison-and-P010-snapshot.md"


class PriorityAuditTests(unittest.TestCase):
    def test_p009_two_prime_palette_not_standard_distance(self):
        pairs=((1,6),(2,5),(3,8),(4,7))
        self.assertEqual(sorted(k for a,b in pairs for k in (a,b)),list(range(1,9)))
        sums={a+b for a,b in pairs}
        self.assertEqual(sums,{7,11})
        self.assertEqual(max(sums)-min(sums),4)
        self.assertNotEqual(max(sums)-min(sums),8)  # 2n
        # Separate primality check for these two prime sums.
        for q in sums:
            self.assertTrue(all(q%d for d in range(2,int(q**.5)+1)))

    def test_p018_six_bases_need_exchange_three_in_example(self):
        a=[
          {2,5,8,21,27},{2,5,8,22,24},
          {2,5,11,21,24},{2,5,11,22,27}
        ]
        b=[{8,21,24,26,30},{11,22,24,26,30}]
        cross=[len(x-y) for x in a for y in b]
        self.assertEqual(min(cross),3)
        self.assertTrue(all(t>=3 for t in cross))
        # Each within-component induced 2-exchange graph must be connected.
        for group in (a,b):
            unseen=set(range(1,len(group)))
            reached={0}
            while unseen:
                new={j for j in unseen
                     if any(len(group[i]-group[j])==2 for i in reached)}
                self.assertTrue(new)
                reached.update(new)
                unseen.difference_update(new)

    def test_p010_pdf_not_committed_in_public_repository(self):
        self.assertIn(
            "3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737",
            AUDIT.read_text(encoding="utf-8"))
        self.assertFalse((ROOT/"coprime_adjacencies(1).pdf").exists())


if __name__=="__main__":
    unittest.main()
