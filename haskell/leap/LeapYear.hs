module LeapYear (isLeapYear) where

isLeapYear :: Int -> Bool
isLeapYear n
  | n `divisibleBy` 400 = True
  | n `divisibleBy` 100 = False
  | n `divisibleBy` 4 = True
  | otherwise = False

divisibleBy :: Int -> Int -> Bool
divisibleBy x y =
  x `mod` y == 0
