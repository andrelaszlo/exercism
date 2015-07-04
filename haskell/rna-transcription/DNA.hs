module DNA (toRNA) where

import qualified Data.Map as Map

type Nucleotide = Char
type Strand = [Nucleotide]

dnaToRna :: Nucleotide -> Nucleotide
dnaToRna nucleotide =
  case Map.lookup nucleotide dnaRnaMap of
    Just rna -> rna
    Nothing -> error "Not a valid DNA nucleotide"
  where dnaRnaMap = Map.fromList $ zip "GCTA" "CGAU"

toRNA :: Strand -> Strand
toRNA = map dnaToRna
