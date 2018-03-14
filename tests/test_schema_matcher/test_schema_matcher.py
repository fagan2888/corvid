import unittest

from corvid.types.table import Token, Cell, Table
from corvid.schema_matcher.pairwise_mapping import PairwiseMapping
from corvid.schema_matcher.schema_matcher import SchemaMatcher


class SchemaMatcherTest(unittest.TestCase):

    def setUp(self):
        self.table_simple = Table.create_from_cells([
            Cell(tokens=[Token(text='subject')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='x')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='y')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='3')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='4')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='z')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='5')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='6')], rowspan=1, colspan=1)
        ], nrow=4, ncol=3)

        self.table_mirror = self.table_simple

        self.table_permute_header = Table.create_from_cells([
            Cell(tokens=[Token(text='subject')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='x')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='z')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='5')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='6')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='y')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='3')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='4')], rowspan=1, colspan=1)
        ], nrow=4, ncol=3)

        self.table_no_header = Table.create_from_cells([
            Cell(tokens=[Token(text='x')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='z')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='5')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='6')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='y')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='3')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='4')], rowspan=1, colspan=1)
        ], nrow=3, ncol=3)

        self.table_only_header = Table.create_from_cells(cells=[
            Cell(tokens=[Token(text='subject')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header2')], rowspan=1, colspan=1)
        ], nrow=1, ncol=3)

        self.table_permute_rows = Table.create_from_cells(cells=[
            Cell(tokens=[Token(text='subject')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='z')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='5')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='6')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='y')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='3')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='4')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='x')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='2')], rowspan=1, colspan=1)
        ], nrow=4, ncol=3)

        self.table_extra_rows = Table.create_from_cells(cells=[
            Cell(tokens=[Token(text='subject')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='x')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='y')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='3')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='4')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='z')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='5')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='6')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='w')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='7')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='8')], rowspan=1, colspan=1)
        ], nrow=5, ncol=3)

        self.table_missing_rows = Table.create_from_cells(cells=[
            Cell(tokens=[Token(text='subject')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='x')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='y')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='3')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='4')], rowspan=1, colspan=1)
        ], nrow=3, ncol=3)

    def test_aggregate_tables(self):
        schema_matcher = SchemaMatcher()

        target_schema = Table.create_from_cells(cells=[
            Cell(tokens=[Token(text='subject')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='not_copied')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='not_copied')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='not_copied')], rowspan=1, colspan=1)
        ], nrow=2, ncol=3)

        pred_aggregate_table = schema_matcher.aggregate_tables(
            pairwise_mappings=[
                PairwiseMapping(self.table_simple, target_schema,
                                score=-999, column_mappings=[(1, 2), (2, 1)])
            ],
            target_schema=target_schema)

        gold_aggregate_table = Table.create_from_cells([
            Cell(tokens=[Token(text='subject')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='header2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='x')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='2')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='1')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='y')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='4')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='3')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='z')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='6')], rowspan=1, colspan=1),
            Cell(tokens=[Token(text='5')], rowspan=1, colspan=1)
        ], nrow=4, ncol=3)

        print(pred_aggregate_table)
        print(gold_aggregate_table)
        self.assertEquals(pred_aggregate_table, gold_aggregate_table)

    def test_aggregate_tables_order(self):
        # test correct ordering of 3+ tables
        pass