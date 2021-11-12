#!/usr/bin/env python
"""
 Copyright (C) 2021 Rostlab
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.
 
 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# -*- coding: utf-8 -*-

from pathlib import Path
import torch


VESPA = "VESPA"
VESPAL = "VESPAl"

MODEL_PATH_DICT = {
    VESPA: Path("models/VESPA-10LR_Cons_Blsm_Prob.pkl"),
    VESPAL: Path("models/VESPAl-10LR_Cons_Blsm.pkl"),
    "CONSCNN": Path("models/ProtT5cons_checkpoint.pt"),
}

OUTPUT_MAP_NAME = "map.json"

# Special character preprended to all "start of span" (for us: every AA as we only do 1-token spans)
# https://huggingface.co/transformers/v3.1.0/_modules/transformers/tokenization_t5.html
SPIECE_UNDERLINE = "▁"

CACHE_DIR = Path("./cache")

TRANSFORMER_LINK = "Rostlab/prot_t5_xl_uniref50"

REPLACE_RARE_AA = True

MUTANT_ORDER = "ALGVSREDTIPKFQNYMHWC" if REPLACE_RARE_AA else "ALGVSREDTIPKFQNYMHWCUZO"
CSV_SEP = ";"
RESULT_PREC = -1  # -1 for all comma positions, positive int for cut precision

NUM_MUTATION_SCORES = 9

VERBOSE = True

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
EMBEDDING_HALF_PREC = True
