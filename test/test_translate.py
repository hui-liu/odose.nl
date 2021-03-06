from Bio import SeqIO
import logging
import unittest

from select_taxa import select_genomes_by_ids
import translate


class Test(unittest.TestCase):

    def setUp(self):
        self.longMessage = True
        logging.root.setLevel(logging.DEBUG)

    def test_translate_genomes(self):
        # Select genomes
        genomes = select_genomes_by_ids(['13305.1']).values()

        # Call translate
        dnafiles, aafiles = translate.translate_genomes(genomes)

        # Verify expected output
        first_header = '13305.1|NC_008253.1|YP_667942.1|None|thr'
        first = next(SeqIO.parse(dnafiles[0], 'fasta'))
        self.assertEqual(first_header, first.id)
        first = next(SeqIO.parse(aafiles[0], 'fasta'))
        self.assertEqual(first_header, first.id)

        # Verify no header appears twice
        headers = [record.id for record in SeqIO.parse(aafiles[0], 'fasta')]
        self.assertEqual(len(headers), len(set(headers)))

    def test_translate_93125_2(self):
        # Select genomes
        genomes = select_genomes_by_ids(['93125.2']).values()

        # Call translate
        aafiles = translate.translate_genomes(genomes)[1]

        # Verify no header appears twice
        headers = [record.id for record in SeqIO.parse(aafiles[0], 'fasta')]
        self.assertEqual(len(headers), len(set(headers)))