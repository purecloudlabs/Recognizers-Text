# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import pytest
from recognizers_text import Culture
from recognizers_number.number.number_recognizer import recognize_number, recognize_ordinal, recognize_percentage

def test_recognize_number_hungarian():
    assert len(recognize_number('42', Culture.Hungarian)) == 1
    assert len(recognize_number('negyvenkettő', Culture.Hungarian)) == 1
    assert len(recognize_number('száz', Culture.Hungarian)) == 1
    assert len(recognize_number('ezerötszáz', Culture.Hungarian)) == 1
    assert len(recognize_number('egy millió', Culture.Hungarian)) == 1
    assert len(recognize_number('1,5', Culture.Hungarian)) == 1
    assert len(recognize_number('egy egész öt', Culture.Hungarian)) == 1
    assert len(recognize_number('mínusz 123', Culture.Hungarian)) == 1
    assert len(recognize_number('negatív 100', Culture.Hungarian)) == 1

def test_recognize_ordinal_hungarian():
    assert len(recognize_ordinal('1.', Culture.Hungarian)) == 1
    assert len(recognize_ordinal('első', Culture.Hungarian)) == 1
    assert len(recognize_ordinal('második', Culture.Hungarian)) == 1
    assert len(recognize_ordinal('harmadik', Culture.Hungarian)) == 1
    assert len(recognize_ordinal('huszonegyedik', Culture.Hungarian)) == 1
    assert len(recognize_ordinal('századik', Culture.Hungarian)) == 1
    assert len(recognize_ordinal('ezredik', Culture.Hungarian)) == 1

def test_recognize_percentage_hungarian():
    assert len(recognize_percentage('100%', Culture.Hungarian)) == 1
    assert len(recognize_percentage('100 százalék', Culture.Hungarian)) == 1
    assert len(recognize_percentage('száz százalék', Culture.Hungarian)) == 1
    assert len(recognize_percentage('száz százaléka', Culture.Hungarian)) == 1