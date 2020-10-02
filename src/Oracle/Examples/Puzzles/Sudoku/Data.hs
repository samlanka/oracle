{-
Copyright (c) 2020 Microsoft Corporation. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Daniel Selsam
-}

{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE LambdaCase #-}
module Oracle.Examples.Puzzles.Sudoku.Data where

import Oracle.Data.Embeddable
import Oracle.Control.Monad.Search

import Oracle.Search.Decision (Decision(Decision))
import Oracle.Search.Replay (replay)

import Oracle.Data.Grid.Index (Index(Index))
import qualified Oracle.Data.Grid.Index as Index

import Oracle.Examples.Puzzles.Sudoku.Board (Board(Board), Value(Value), SubgridIndex(SubgridIndex))
import qualified Oracle.Examples.Puzzles.Sudoku.Board as Board

import Oracle.Examples.Puzzles.Sudoku.Solve (SolveM, solve, selectRCV, selectVRC, selectOIV, selectEmpty)

import Control.Monad.Reader (ReaderT, runReaderT, ask, asks)
import Control.Monad.State (StateT, evalStateT, execStateT, runStateT, get, gets, put, modify)
import Control.Monad.Identity (Identity, runIdentity)
import Control.Monad.Random.Class (getRandomR)

import qualified Data.Set as Set

type GenM = ReaderT Board (StateT Board IO)

data SearchPair = SearchPair {
  fselect :: SolveM (),
  fgen    :: Index -> GenM [Int]
  }

searchPairs :: [SearchPair]
searchPairs = [
  SearchPair selectRCV   genStepRCV,
  SearchPair selectVRC   genStepVRC,
  SearchPair selectOIV   genStepOIV,
  SearchPair selectEmpty genStepEmpty
  ]

genData :: Board -> Board -> SearchPair -> IO [Decision]
genData start end (SearchPair fselect fgen) = do
  choiceIdxs <- evalStateT (runReaderT (gen fgen) end) start
  pure . runIdentity $ replay (execStateT (solve fselect) start) choiceIdxs

gen :: (Index -> GenM [Int]) -> GenM [Int]
gen f = Board.isFilled >>= \case
  True   -> pure []
  False  -> do
    current  <- get
    i        <- getRandomR (0, Set.size (Board.empty current) - 1)
    choices  <- f $ Set.elemAt i (Board.empty current)
    rest     <- gen f
    pure $ choices ++ rest

genStepRCV :: Index -> GenM [Int]
genStepRCV idx@(Index r c) = do
  Value x  <- Board.readIdx idx
  pure [r, c, x - 1]

genStepVRC :: Index -> GenM [Int]
genStepVRC idx@(Index r c) = do
  Value x  <- Board.readIdx idx
  pure [x-1, r, c]

genStepOIV :: Index -> GenM [Int]
genStepOIV idx = do
  let SubgridIndex (Index oi oj) (Index ii ij) = Board.idx2subgrid idx
  Value x <- Board.readIdx idx
  pure [oi, oj, ii, ij, x - 1]

genStepEmpty :: Index -> GenM [Int]
genStepEmpty idx = do
  empty <- gets Board.empty
  let i = Set.findIndex idx empty
  Value x <- Board.readIdx idx
  pure [i, x - 1]
