#!/usr/bin/env python3

"""Test module for json_converter.py"""

import unittest
import pycg

class JSONConverterTestCase(unittest.TestCase):
    """Unit tests for json_converter.py; Tests inspired by wrestlers in:
    https://en.wikipedia.org/wiki/Dusty_Rhodes_Tag_Team_Classic#2019_tournament"""

    def test_primitives(self):
        """Primitive JSON types"""
        self.assertEqual(pycg.rprint(False), "false")
        self.assertEqual(pycg.rprint(True), "true")
        self.assertEqual(pycg.rprint(0), "0")
        self.assertEqual(pycg.rprint(3.14), "3.14")
        self.assertEqual(pycg.rprint("testing"), '"testing"')

    def test_list(self):
        """List functionality"""
        self.assertEqual(pycg.rprint([]), "[]")
        self.assertEqual(pycg.rprint(["aichner", "barthel"]), '[\n    "aichner",\n    "barthel"\n]')

    def test_dict(self):
        """Dict functionality"""
        self.assertEqual(pycg.rprint({}), "{}")
        self.assertEqual(pycg.rprint({"lorcan": 1, "birch": 2}),\
            '{\n    "lorcan": 1,\n    "birch": 2\n}')

    def test_tuple(self):
        """Tuples are not allowed"""
        self.assertRaises(Exception, pycg.rprint, ("blake", "cutler", "ryker"))

    def test_nests(self):
        """Nested lists and objects"""
        undisputed = {
            "Name": "Undisputed Era",
            "Members": [
                {
                    "Name": "Adam Cole",
                    "Leader": True,
                    "Gimmick": "BAY BAY"
                },
                {
                    "Name": "Roderick Strong",
                    "Leader": False,
                    "Gimmick": "The Messiah of the Backbreaker"
                },
                {
                    "Name": "Kyle O-Reilly",
                    "Leader": False,
                    "Gimmick": "Air guitar"
                },
                {
                    "Name": "Bobby Fish",
                    "Leader": False,
                    "Gimmick": "???"
                }
            ]
        }
        parsed = """{
    "Name": "Undisputed Era",
    "Members": [
        {
            "Name": "Adam Cole",
            "Leader": true,
            "Gimmick": "BAY BAY"
        },
        {
            "Name": "Roderick Strong",
            "Leader": false,
            "Gimmick": "The Messiah of the Backbreaker"
        },
        {
            "Name": "Kyle O-Reilly",
            "Leader": false,
            "Gimmick": "Air guitar"
        },
        {
            "Name": "Bobby Fish",
            "Leader": false,
            "Gimmick": "???"
        }
    ]
}"""
        self.assertEqual(pycg.rprint(undisputed), parsed)

    def test_py_to_js(self):
        """Testing wrapper function"""
        diy = '{"Name":"#DIY", "Members":["Gargano", "Ciampa"]}'
        parsed = '{\n    "Name": "#DIY",\n    "Members": [\n        "Gargano",\n' +\
        '        "Ciampa"\n    ]\n}'
        self.assertEqual(pycg.py_to_js(diy), parsed)

if __name__ == "__main__": # pragma: no cover
    unittest.main()
